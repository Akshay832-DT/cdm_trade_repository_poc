"""
Test FIX message parsing using generated Pydantic models.
"""
import unittest
import asyncio
from datetime import datetime, date
from src.parsers.controller import ParserController
from src.models.fix.generated.messages.bidresponse import BidResponse
from src.models.fix.generated.components.bidcomprspgrp import NoBidComponents

class TestFIXParser(unittest.TestCase):
    """Test FIX message parsing functionality."""
    
    def setUp(self):
        self.parser_controller = ParserController()
    
    def test_bid_response_parsing(self):
        """Test parsing a BidResponse message."""
        # Raw FIX message string (pipe symbol as separator for readability, will be replaced with SOH)
        raw_fix_message = (
            "8=FIX.4.4|9=489|35=l|34=1|49=SENDER|56=TARGET|52=20240412-14:30:00|"
            # BidResponse fields
            "390=BID123|391=CLIENT123|398=0|"
            # Instrument fields
            "55=AAPL|48=US0378331005|22=8|167=CS|200=202412|541=20241231|15=USD|"
            # Parties fields
            "453=1|448=PARTY123|447=D|452=1|"
            # BidComponents fields
            "420=1|66=LIST123|421=US|54=1|44=100.50|423=1|406=101.25|430=1|63=0|"
            "64=20241231|336=TSE1|625=MORNING|58=Sample bid component|"
            # CommissionData fields within BidComponents
            "12=1.25|13=1|479=USD|10=123"
        ).replace("|", "\x01")  # Replace pipe with SOH character
        
        # Parse the message asynchronously
        message = asyncio.run(self.parser_controller.parse_message(raw_fix_message, 'FIX'))
        
        # Verify message is correctly parsed as BidResponse
        self.assertIsInstance(message, BidResponse)
        
        # Verify header fields
        self.assertEqual(message.begin_string, "FIX.4.4")
        self.assertEqual(message.msg_type, "l")
        self.assertEqual(message.sender_comp_id, "SENDER")
        self.assertEqual(message.target_comp_id, "TARGET")
        self.assertEqual(message.msg_seq_num, 1)
        
        # Verify BidResponse fields
        self.assertEqual(message.bid_id, "BID123")
        self.assertEqual(message.client_bid_id, "CLIENT123")
        
        # Verify Instrument fields
        self.assertEqual(message.instrument.symbol, "AAPL")
        self.assertEqual(message.instrument.security_id, "US0378331005")
        self.assertEqual(message.instrument.security_id_source, "8")
        self.assertEqual(message.instrument.security_type, "CS")
        self.assertEqual(message.instrument.currency, "USD")
        
        # Verify Parties fields
        self.assertEqual(message.parties.no_party_ids, 1)
        self.assertEqual(message.parties.no_party_ids_items[0].party_id, "PARTY123")
        self.assertEqual(message.parties.no_party_ids_items[0].party_id_source, "D")
        self.assertEqual(message.parties.no_party_ids_items[0].party_role, 1)
        
        # Verify BidComponents fields
        self.assertEqual(message.bid_comp_rsp_grp.no_bid_components, 1)
        bid_component = message.bid_comp_rsp_grp.no_bid_components_items[0]
        self.assertEqual(bid_component.list_id, "LIST123")
        self.assertEqual(bid_component.country, "US")
        self.assertEqual(bid_component.side, "1")
        self.assertEqual(bid_component.price, 100.50)
        self.assertEqual(bid_component.price_type, 1)
        self.assertEqual(bid_component.fair_value, 101.25)
        self.assertEqual(bid_component.net_gross_ind, 1)
        self.assertEqual(bid_component.settl_type, "0")
        self.assertEqual(bid_component.settl_date, date(2024, 12, 31))
        self.assertEqual(bid_component.trading_session_id, "TSE1")
        self.assertEqual(bid_component.trading_session_sub_id, "MORNING")
        self.assertEqual(bid_component.text, "Sample bid component")
        
        # Verify CommissionData fields
        self.assertEqual(bid_component.commission_data.commission, 1.25)
        self.assertEqual(bid_component.commission_data.comm_type, "1")
        self.assertEqual(bid_component.commission_data.comm_currency, "USD")

if __name__ == '__main__':
    unittest.main() 