from typing import Dict, Any, Optional
import json
import yaml
from pathlib import Path
from ...models.base import BaseParser, TradeModel
from ...models.cdm.generated import CDMTrade
import logging

class CDMParser(BaseParser):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.mappings = self._load_mappings()

    def _load_mappings(self) -> Dict:
        config_path = Path(__file__).parent / 'config' / 'cdm64_mappings.yaml'
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    async def validate(self, message: str) -> bool:
        try:
            data = json.loads(message)
            return self._validate_cdm_structure(data)
        except json.JSONDecodeError as e:
            self.logger.error(f"CDM validation error: {str(e)}")
            return False

    def _validate_cdm_structure(self, data: Dict) -> bool:
        if not isinstance(data, dict):
            return False
        
        # Check for required top-level fields
        required_fields = ['trade', 'event', 'lifecycle']
        return any(field in data for field in required_fields)

    async def parse(self, message: str) -> TradeModel:
        data = json.loads(message)
        
        # Determine message type
        message_type = next((k for k in ['trade', 'event', 'lifecycle'] if k in data), None)
        if not message_type:
            raise ValueError("Invalid CDM message structure")
        
        # Parse according to message type
        if message_type == 'trade':
            return CDMTrade(**data['trade'])
        elif message_type == 'event':
            return CDMEvent(**data['event'])
        else:
            return CDMLifecycle(**data['lifecycle'])

    def _parse_fields(self, data: Dict, mapping: Dict) -> Dict[str, Any]:
        result = {}
        for field_name, field_path in mapping.items():
            if isinstance(field_path, dict):
                sub_data = data.get(field_name, {})
                result[field_name] = self._parse_fields(sub_data, field_path)
            else:
                value = data.get(field_path)
                if value is not None:
                    result[field_name] = value
        return result 