from typing import Dict, Optional
from .base import BaseParser
from .fix.parser import FIXParser
from .fpml.parser import FpMLParser
from .cdm.parser import CdmParser
from ..models.base import TradeModel
import yaml
import logging

class ParserController:
    def __init__(self):
        self.parsers: Dict[str, BaseParser] = {
            'FIX': FIXParser(),
            'FPML': FpMLParser(),
            'CDM': CdmParser()
        }
        self.logger = logging.getLogger(__name__)

    async def parse_message(self, message: str, format_type: str) -> TradeModel:
        if format_type not in self.parsers:
            raise ValueError(f"Unsupported format: {format_type}")

        parser = self.parsers[format_type]
        
        try:
            if not await parser.validate(message):
                raise ValueError(f"Invalid {format_type} message format")
            
            return await parser.parse(message)
        except Exception as e:
            self.logger.error(f"Error parsing {format_type} message: {str(e)}")
            raise

    def get_supported_formats(self) -> list[str]:
        return list(self.parsers.keys()) 