from typing import Dict, Any, Optional, Type
import simplefix
import yaml
import importlib
from pathlib import Path
from datetime import datetime
from ...models.base import BaseParser, TradeModel
from ...models.fix.base import FIXMessageBase
from ...models.fix.messages.message_types import MessageType
import logging

class FIXParser(BaseParser):
    def __init__(self):
        self.parser = simplefix.FixParser()
        self.logger = logging.getLogger(__name__)
        self.mappings = self._load_mappings()
        self.message_type_models = self._load_message_type_models()

    def _load_mappings(self) -> Dict:
        config_path = Path(__file__).parent / 'config' / 'fix44_mappings.yaml'
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def _load_message_type_models(self) -> Dict[str, Type[FIXMessageBase]]:
        """
        Dynamically load and map all generated message models.
        
        Returns:
            Dict[str, Type[FIXMessageBase]]: Dictionary mapping message types to model classes
        """
        result = {}
        try:
            # Dynamically import all message models
            messages_module = importlib.import_module('models.fix.generated.messages')
            
            # Map each message type to its model class
            for msg_type in MessageType:
                msg_name = msg_type.name
                try:
                    model_class = getattr(messages_module, msg_name)
                    result[msg_type.value] = model_class
                except AttributeError:
                    self.logger.warning(f"No model found for message type {msg_type.value} ({msg_name})")
        except ImportError as e:
            self.logger.error(f"Error importing message models: {str(e)}")
        
        return result

    async def validate(self, message: str) -> bool:
        try:
            self.parser.push(message.encode())
            msg = self.parser.get_message()
            return msg is not None and self._validate_message_type(msg)
        except Exception as e:
            self.logger.error(f"FIX validation error: {str(e)}")
            return False

    def _validate_message_type(self, msg: simplefix.FixMessage) -> bool:
        msg_type = msg.get(35)
        if not msg_type:
            return False
        return msg_type.decode() in self.mappings['message_types'] or msg_type.decode() in self.message_type_models

    async def parse(self, message: str) -> TradeModel:
        self.parser.push(message.encode())
        fix_msg = self.parser.get_message()
        
        if not fix_msg:
            raise ValueError("Invalid FIX message format")
        
        msg_type = fix_msg.get(35).decode()
        
        # Try to find a specific model for this message type
        model_class = self.message_type_models.get(msg_type)
        
        if model_class:
            # Use the specific model for this message type
            parsed_data = self._parse_fields(fix_msg)
            
            # Handle date/time fields
            for field_tag, value in list(parsed_data.items()):
                # Convert timestamps (tag 52 - SendingTime and others)
                if field_tag == '52' and value:
                    try:
                        # FIX timestamps format: YYYYMMDD-HH:MM:SS or YYYYMMDD-HH:MM:SS.sss
                        parsed_data[field_tag] = datetime.strptime(value, '%Y%m%d-%H:%M:%S')
                    except ValueError:
                        try:
                            parsed_data[field_tag] = datetime.strptime(value, '%Y%m%d-%H:%M:%S.%f')
                        except ValueError:
                            # If we can't parse it, keep the original string
                            pass
            
            try:
                # Create the model instance
                return model_class(**parsed_data)
            except Exception as e:
                self.logger.warning(f"Error creating specific model for {msg_type}: {str(e)}")
                # Fall back to generic model
        
        # Fall back to generic FIXMessage
        parsed_data = self._parse_fields(fix_msg)
        return FIXMessageBase(**parsed_data)

    def _parse_fields(self, msg: simplefix.FixMessage) -> Dict[str, Any]:
        result = {}
        for tag in msg:
            try:
                value = msg.get(tag)
                if value:
                    result[str(tag)] = value.decode()
            except Exception as e:
                self.logger.warning(f"Error parsing tag {tag}: {str(e)}")
        return result 