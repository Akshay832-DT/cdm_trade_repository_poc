from typing import Dict, Any, Optional
import xml.etree.ElementTree as ET
import yaml
from pathlib import Path
from ...models.base import BaseParser, TradeModel
from ...models.fpml.generated import FpMLTrade
import logging

class FpMLParser(BaseParser):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.mappings = self._load_mappings()
        self.namespaces = self.mappings['namespaces']

    def _load_mappings(self) -> Dict:
        config_path = Path(__file__).parent / 'config' / 'fpml_mappings.yaml'
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    async def validate(self, message: str) -> bool:
        try:
            root = ET.fromstring(message)
            return self._validate_fpml_structure(root)
        except ET.ParseError as e:
            self.logger.error(f"FpML validation error: {str(e)}")
            return False

    def _validate_fpml_structure(self, root: ET.Element) -> bool:
        # Check namespace
        if not root.tag.startswith('{' + self.namespaces['fpml'] + '}'):
            return False
        
        # Check message type
        message_type = root.tag.split('}')[-1]
        return message_type in self.mappings['message_types'].values()

    async def parse(self, message: str) -> TradeModel:
        root = ET.fromstring(message)
        message_type = root.tag.split('}')[-1]
        
        if message_type not in self.mappings['message_types'].values():
            raise ValueError(f"Unsupported message type: {message_type}")
        
        parsed_data = self._parse_element(root, self.mappings['field_mappings'][message_type])
        return FpMLTrade(**parsed_data)

    def _parse_element(self, element: ET.Element, mapping: Dict) -> Dict[str, Any]:
        result = {}
        for field_name, xpath in mapping.items():
            if isinstance(xpath, dict):
                sub_element = element.find(xpath['path'], self.namespaces)
                if sub_element is not None:
                    result[field_name] = self._parse_element(sub_element, xpath)
            else:
                value = element.find(xpath, self.namespaces)
                if value is not None:
                    result[field_name] = value.text
        return result 