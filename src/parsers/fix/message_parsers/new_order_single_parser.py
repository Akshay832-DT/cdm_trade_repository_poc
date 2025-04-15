"""
Parser for NewOrderSingle messages.
"""
from datetime import datetime
from typing import Dict, Any
import simplefix
import logging

from src.parsers.fix.base_parser import FIXMessageParser
from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent

class NewOrderSingleParser(FIXMessageParser):
    """Parser for NewOrderSingle messages."""
    
    async def parse(self, message: simplefix.FixMessage) -> NewOrderSingleMessage:
        """
        Parse a NewOrderSingle message.
        
        Args:
            message (simplefix.FixMessage): The FIX message to parse
            
        Returns:
            NewOrderSingleMessage: The parsed message model instance
        """
        try:
            # Parse common fields
            fields = await self._parse_common_fields(message)
            
            # Parse message-specific fields
            fields.update({
                'ClOrdID': message.get(11).decode() if message.get(11) else None,
                'Account': message.get(1).decode() if message.get(1) else None,
                'HandlInst': message.get(21).decode() if message.get(21) else None,
                'ExecInst': message.get(18).decode() if message.get(18) else None,
                'MinQty': float(message.get(110).decode()) if message.get(110) else None,
                'MaxFloor': float(message.get(111).decode()) if message.get(111) else None,
                'ExDestination': message.get(100).decode() if message.get(100) else None,
                'ProcessCode': message.get(81).decode() if message.get(81) else None,
                'Side': message.get(54).decode() if message.get(54) else None,
                'TimeInForce': message.get(59).decode() if message.get(59) else None,
                'TransactTime': self._parse_datetime(message.get(60)) if message.get(60) else None,
                'OrdType': message.get(40).decode() if message.get(40) else None,
                'Price': float(message.get(44).decode()) if message.get(44) else None,
                'StopPx': float(message.get(99).decode()) if message.get(99) else None,
                'Currency': message.get(15).decode() if message.get(15) else None,
                'ComplianceID': message.get(376).decode() if message.get(376) else None,
                'Text': message.get(58).decode() if message.get(58) else None,
                'PositionEffect': message.get(77).decode() if message.get(77) else None
            })
            
            # Parse Instrument component
            try:
                instrument_fields = {
                    'Symbol': message.get(55).decode() if message.get(55) else None,
                    'SecurityID': message.get(48).decode() if message.get(48) else None,
                    'SecurityIDSource': message.get(22).decode() if message.get(22) else None,
                    'SecurityExchange': message.get(207).decode() if message.get(207) else None,
                    'StrikeCurrency': message.get(947).decode() if message.get(947) else None
                }
                
                # Only add the component if at least one field is not None
                if any(v is not None for v in instrument_fields.values()):
                    fields['Instrument'] = InstrumentComponent(**{k: v for k, v in instrument_fields.items() if v is not None})
            except Exception as e:
                self.logger.error(f"Error creating Instrument component: {str(e)}")
                raise
            
            # Parse OrderQtyData component
            try:
                orderqty_fields = {
                    'OrderQty': float(message.get(38).decode()) if message.get(38) else None,
                    'CashOrderQty': float(message.get(152).decode()) if message.get(152) else None
                }
                
                # Only add the component if at least one field is not None
                if any(v is not None for v in orderqty_fields.values()):
                    fields['OrderQtyData'] = OrderQtyDataComponent(**{k: v for k, v in orderqty_fields.items() if v is not None})
            except Exception as e:
                self.logger.error(f"Error creating OrderQtyData component: {str(e)}")
                raise
            
            return NewOrderSingleMessage(**fields)
            
        except Exception as e:
            self.logger.error(f"Error parsing NewOrderSingle message: {str(e)}")
            raise 

    def _parse_datetime(self, value: bytes) -> datetime:
        """
        Parse datetime from bytes, supporting multiple formats.
        
        Args:
            value (bytes): The datetime value to parse
            
        Returns:
            datetime: The parsed datetime
        """
        if not value:
            return None
            
        value_str = value.decode()
        try:
            return datetime.strptime(value_str, '%Y%m%d-%H:%M:%S.%f')
        except ValueError:
            try:
                return datetime.strptime(value_str, '%Y%m%d-%H:%M:%S')
            except ValueError:
                self.logger.warning(f"Could not parse datetime: {value_str}")
                return None 