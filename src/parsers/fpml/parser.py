from typing import Dict, Any, Optional, List
import xml.etree.ElementTree as ET
import yaml
from pathlib import Path
from datetime import datetime, date
import re
from ...models.base import BaseParser, TradeModel
from ...models.fpml.generated import FpMLTrade
import logging

class FpMLParser(BaseParser):
    """Parser for FpML messages."""
    
    def __init__(self):
        """Initialize the FpML parser."""
        self.logger = logging.getLogger(__name__)
        self.mappings = self._load_mappings()
        self.namespaces = self.mappings['namespaces']

    def _load_mappings(self) -> Dict:
        """Load FpML mappings from config file."""
        config_path = Path(__file__).parent / 'config' / 'fpml_mappings.yaml'
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    async def validate(self, message: str) -> bool:
        """
        Validate an FpML message.
        
        Args:
            message: FpML XML message string
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            root = ET.fromstring(message)
            
            # Check namespace
            if not root.tag.startswith('{' + self.namespaces['fpml'] + '}'):
                self.logger.warning(f"Invalid FpML namespace: {root.tag}")
                return False
            
            # Check message type
            message_type = root.tag.split('}')[-1]
            if message_type not in self.mappings['message_types'].values():
                self.logger.warning(f"Unsupported message type: {message_type}")
                return False
            
            # Check required elements
            # First look for trade element
            trade_elem = root.find('.//{' + self.namespaces['fpml'] + '}trade')
            if trade_elem is None:
                self.logger.warning("Missing required element: trade")
                return False
            
            # Check trade header
            trade_header = trade_elem.find('.//{' + self.namespaces['fpml'] + '}tradeHeader')
            if trade_header is None:
                self.logger.warning("Missing required element: tradeHeader")
                return False
            
            # Check party trade identifier
            party_trade_id = trade_header.find('.//{' + self.namespaces['fpml'] + '}partyTradeIdentifier')
            if party_trade_id is None:
                self.logger.warning("Missing required element: partyTradeIdentifier")
                return False
            
            # Check trade date
            trade_date = trade_header.find('.//{' + self.namespaces['fpml'] + '}tradeDate')
            if trade_date is None:
                self.logger.warning("Missing required element: tradeDate")
                return False
            
            # Check product
            product = trade_elem.find('.//{' + self.namespaces['fpml'] + '}product')
            if product is None:
                self.logger.warning("Missing required element: product")
                return False
            
            return True
        except ET.ParseError as e:
            self.logger.error(f"XML parsing error: {str(e)}")
            return False
        except Exception as e:
            self.logger.error(f"Validation error: {str(e)}")
            return False

    async def parse(self, message: str) -> TradeModel:
        """
        Parse an FpML message into a Pydantic model.
        
        Args:
            message: FpML XML message string
            
        Returns:
            TradeModel: Parsed trade model
        """
        try:
            root = ET.fromstring(message)
            
            # First get trade element
            trade_elem = root.find('.//{' + self.namespaces['fpml'] + '}trade')
            if trade_elem is None:
                raise ValueError("Missing required element: trade")
            
            # Parse the trade element
            parsed_data = self._parse_trade(trade_elem)
            
            # Create FpMLTrade model
            return FpMLTrade(**parsed_data)
        except ET.ParseError as e:
            self.logger.error(f"XML parsing error: {str(e)}")
            raise
        except Exception as e:
            self.logger.error(f"Parsing error: {str(e)}")
            raise

    def _parse_trade(self, trade_elem: ET.Element) -> Dict[str, Any]:
        """
        Parse trade element into a dictionary.
        
        Args:
            trade_elem: XML Element representing trade
            
        Returns:
            Dict: Parsed trade data
        """
        result = {}
        
        # Parse trade header
        trade_header = trade_elem.find('.//{' + self.namespaces['fpml'] + '}tradeHeader')
        if trade_header is not None:
            result['tradeHeader'] = self._parse_trade_header(trade_header)
        
        # Parse product
        product = trade_elem.find('.//{' + self.namespaces['fpml'] + '}product')
        if product is not None:
            result['product'] = self._parse_product(product)
        
        return result

    def _parse_trade_header(self, header_elem: ET.Element) -> Dict[str, Any]:
        """Parse trade header element."""
        result = {}
        
        # Parse party trade identifier elements
        party_ids = []
        for party_id_elem in header_elem.findall('.//{' + self.namespaces['fpml'] + '}partyTradeIdentifier'):
            party_ref = party_id_elem.find('.//{' + self.namespaces['fpml'] + '}partyReference')
            trade_id = party_id_elem.find('.//{' + self.namespaces['fpml'] + '}tradeId')
            
            if party_ref is not None and trade_id is not None:
                party_ids.append({
                    'partyReference': {'href': party_ref.get('href')},
                    'tradeId': trade_id.text
                })
        
        if party_ids:
            result['partyTradeIdentifier'] = party_ids
        
        # Parse trade date
        trade_date = header_elem.find('.//{' + self.namespaces['fpml'] + '}tradeDate')
        if trade_date is not None and trade_date.text:
            result['tradeDate'] = self._parse_date(trade_date.text)
        
        # Parse cleared date (optional)
        cleared_date = header_elem.find('.//{' + self.namespaces['fpml'] + '}clearedDate')
        if cleared_date is not None and cleared_date.text:
            result['clearedDate'] = self._parse_date(cleared_date.text)
        
        return result

    def _parse_product(self, product_elem: ET.Element) -> Dict[str, Any]:
        """Parse product element."""
        result = {}
        
        # Check for interest rate product
        interest_rate = product_elem.find('.//{' + self.namespaces['fpml'] + '}interestRate')
        if interest_rate is not None:
            result['interestRate'] = self._parse_interest_rate(interest_rate)
        
        # Check for credit product
        credit = product_elem.find('.//{' + self.namespaces['fpml'] + '}credit')
        if credit is not None:
            result['credit'] = self._parse_credit(credit)
        
        return result

    def _parse_interest_rate(self, ir_elem: ET.Element) -> Dict[str, Any]:
        """Parse interest rate product element."""
        result = {}
        
        # Parse swap streams
        swap_streams = []
        for stream_elem in ir_elem.findall('.//{' + self.namespaces['fpml'] + '}swapStream'):
            stream_data = {}
            
            # Parse payer/receiver
            payer_receiver_elem = stream_elem.find('.//{' + self.namespaces['fpml'] + '}payerReceiver')
            if payer_receiver_elem is not None:
                payer_ref = payer_receiver_elem.find('.//{' + self.namespaces['fpml'] + '}payerPartyReference')
                receiver_ref = payer_receiver_elem.find('.//{' + self.namespaces['fpml'] + '}receiverPartyReference')
                
                stream_data['payerReceiver'] = {
                    'payerPartyReference': {'href': payer_ref.get('href')} if payer_ref is not None else None,
                    'receiverPartyReference': {'href': receiver_ref.get('href')} if receiver_ref is not None else None
                }
            
            # Parse payment frequency
            payment_freq = stream_elem.find('.//{' + self.namespaces['fpml'] + '}paymentFrequency')
            if payment_freq is not None and payment_freq.text:
                stream_data['paymentFrequency'] = payment_freq.text
            
            # Parse notional amount
            notional_elem = stream_elem.find('.//{' + self.namespaces['fpml'] + '}notionalAmount')
            if notional_elem is not None:
                amount = notional_elem.find('.//{' + self.namespaces['fpml'] + '}amount')
                currency = notional_elem.find('.//{' + self.namespaces['fpml'] + '}currency')
                
                stream_data['notionalAmount'] = {
                    'amount': float(amount.text) if amount is not None and amount.text else 0.0,
                    'currency': currency.text if currency is not None and currency.text else ''
                }
            
            swap_streams.append(stream_data)
        
        if swap_streams:
            result['swapStream'] = swap_streams
        
        return result

    def _parse_credit(self, credit_elem: ET.Element) -> Dict[str, Any]:
        """Parse credit product element."""
        result = {}
        
        # Parse protection terms
        protection_terms = credit_elem.find('.//{' + self.namespaces['fpml'] + '}protectionTerms')
        if protection_terms is not None:
            result['protectionTerms'] = {
                'referenceEntity': self._get_element_text(protection_terms, 'referenceEntity'),
                'creditEvent': self._get_element_text(protection_terms, 'creditEvent'),
                'settlementType': self._get_element_text(protection_terms, 'settlementType')
            }
        
        # Parse reference information
        ref_info = credit_elem.find('.//{' + self.namespaces['fpml'] + '}referenceInformation')
        if ref_info is not None:
            result['referenceInformation'] = {
                'referenceEntity': self._get_element_text(ref_info, 'referenceEntity'),
                'referenceObligation': self._get_element_text(ref_info, 'referenceObligation')
            }
        
        return result

    def _get_element_text(self, parent: ET.Element, tag_name: str) -> Optional[str]:
        """Get text from an element by its tag name."""
        elem = parent.find('.//{' + self.namespaces['fpml'] + '}' + tag_name)
        return elem.text if elem is not None and elem.text else None

    def _parse_date(self, date_str: str) -> date:
        """Parse date string in YYYY-MM-DD format."""
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            self.logger.warning(f"Invalid date format: {date_str}")
            return None 