"""
Parser for BidResponse messages.
"""
from datetime import datetime
from typing import Dict, Any
import simplefix
import logging

from src.parsers.fix.base_parser import FIXMessageParser
from src.models.fix.generated.messages.bidresponse import BidResponseMessage
from src.models.fix.generated.components.commissiondata import CommissionDataComponent
from src.models.fix.generated.components.bidcomprspgrp import NoBidComponentsGroup, BidCompRspGrpComponent

class BidResponseParser(FIXMessageParser):
    """Parser for BidResponse messages."""
    
    async def parse(self, message: simplefix.FixMessage) -> BidResponseMessage:
        """
        Parse a BidResponse message.
        
        Args:
            message (simplefix.FixMessage): The FIX message to parse
            
        Returns:
            BidResponseMessage: The parsed message model instance
        """
        try:
            # Parse common fields
            fields = await self._parse_common_fields(message)
            
            # Parse message-specific fields
            fields.update({
                'BidID': message.get(390).decode() if message.get(390) else None,
                'ClientBidID': message.get(391).decode() if message.get(391) else None,
                'BidRequestTransType': message.get(374).decode() if message.get(374) else None,
                'ListID': message.get(66).decode() if message.get(66) else None,
                'Text': message.get(58).decode() if message.get(58) else None,
                'EncodedTextLen': int(message.get(354).decode()) if message.get(354) else None,
                'EncodedText': message.get(355).decode() if message.get(355) else None,
                'NoBidComponents': int(message.get(420).decode()) if message.get(420) else None
            })
            
            # Parse Commission component
            try:
                commission_fields = {
                    'Commission': float(message.get(12).decode()) if message.get(12) else None,
                    'CommType': message.get(13).decode() if message.get(13) else None,
                    'CommCurrency': message.get(479).decode() if message.get(479) else None,
                    'FundRenewWaiv': message.get(497).decode() if message.get(497) else None
                }
                # Only add the component if at least one field is not None
                if any(v is not None for v in commission_fields.values()):
                    fields['CommissionData'] = CommissionDataComponent(**{k: v for k, v in commission_fields.items() if v is not None})
            except Exception as e:
                self.logger.error(f"Error creating CommissionData component: {str(e)}")
                raise
            
            # Parse BidCompRspGrp component
            try:
                # Create items for NoBidComponents repeating group
                if fields.get('NoBidComponents') and int(fields['NoBidComponents']) > 0:
                    # For simplicity, assuming all relevant fields for the group are in the main message
                    group_items = []
                    
                    # In reality, you would need to extract repeating group fields from the message
                    # This is a simplified example - in a real implementation, you'd need to properly
                    # extract repeating groups from the FIX message
                    group_item = {
                        'Commission': float(message.get(12).decode()) if message.get(12) else None,
                        'CommType': message.get(13).decode() if message.get(13) else None,
                        'ListID': message.get(66).decode() if message.get(66) else None,
                        'Country': message.get(421).decode() if message.get(421) else None,
                        'Side': message.get(54).decode() if message.get(54) else None,
                        'Price': float(message.get(44).decode()) if message.get(44) else None,
                        'PriceType': message.get(423).decode() if message.get(423) else None,
                        'FairValue': float(message.get(406).decode()) if message.get(406) else None,
                        'NetGrossInd': message.get(430).decode() if message.get(430) else None,
                        'SettlType': message.get(63).decode() if message.get(63) else None,
                        'SettlDate': datetime.strptime(message.get(64).decode(), '%Y%m%d') if message.get(64) else None,
                        'TradingSessionID': message.get(336).decode() if message.get(336) else None,
                        'Text': message.get(58).decode() if message.get(58) else None,
                    }
                    
                    # Only add items with at least one non-None value
                    if any(v is not None for v in group_item.values()):
                        group_items.append(NoBidComponentsGroup(**{k: v for k, v in group_item.items() if v is not None}))
                    
                    if group_items:
                        fields['BidCompRspGrp'] = BidCompRspGrpComponent(
                            NoBidComponents=len(group_items),
                            NoBidComponents_items=group_items
                        )
            except Exception as e:
                self.logger.error(f"Error creating BidCompRspGrp component: {str(e)}")
                raise
            
            return BidResponseMessage(**fields)
            
        except Exception as e:
            self.logger.error(f"Error parsing BidResponse message: {str(e)}")
            raise 