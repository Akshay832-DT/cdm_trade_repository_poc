"""
Test FIX BidResponse message creation and validation.
"""
import pytest
from datetime import datetime, date
from src.models.fix.generated.messages.bidresponse import BidResponse, BidResponseComponent

def test_bidresponse_message_creation():
    # Create a sample BidResponse message
    bid_response = BidResponse(
        # Standard header fields
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=12345,
        SendingTime=datetime.now(),
        
        # Message-specific fields
        BidID="BID123",
        ClientBidID="CLIENT456",
        NoBidComponents=2,
        
        # Create bid components
        BidComponents=[
            BidResponseComponent(
                Commission=0.5,
                CommType="2",  # 2 = Percentage
                CommCurrency="USD",
                FundRenewWaiv="N",  # N = No
                ListID="LIST001",
                Country="US",
                Side="1",  # 1 = Buy
                Price=100.25,
                PriceType=1,  # 1 = Percentage
                FairValue=100.30,
                NetGrossInd=1,  # 1 = Net
                SettlType="0",  # 0 = Regular
                SettlDate=date(2024, 12, 31),
                TradingSessionID="TSE1",
                TradingSessionSubID="MORNING",
                Text="First bid component"
            ),
            BidResponseComponent(
                Commission=0.6,
                CommType="2",
                CommCurrency="USD",
                FundRenewWaiv="N",
                ListID="LIST002",
                Country="UK",
                Side="2",  # 2 = Sell
                Price=100.35,
                PriceType=1,
                FairValue=100.40,
                NetGrossInd=1,
                SettlType="0",
                SettlDate=date(2024, 12, 31),
                TradingSessionID="TSE1",
                TradingSessionSubID="AFTERNOON",
                Text="Second bid component"
            )
        ]
    )
    
    # Validate the message
    assert bid_response.SenderCompID == "SENDER"
    assert bid_response.TargetCompID == "TARGET"
    assert bid_response.MsgType == "l"  # BidResponse message type
    assert bid_response.BidID == "BID123"
    assert bid_response.ClientBidID == "CLIENT456"
    assert bid_response.NoBidComponents == 2
    
    # Validate first component
    comp1 = bid_response.BidComponents[0]
    assert comp1.Commission == 0.5
    assert comp1.CommType == "2"
    assert comp1.Side == "1"
    assert comp1.Price == 100.25
    assert comp1.Text == "First bid component"
    
    # Validate second component
    comp2 = bid_response.BidComponents[1]
    assert comp2.Commission == 0.6
    assert comp2.CommType == "2"
    assert comp2.Side == "2"
    assert comp2.Price == 100.35
    assert comp2.Text == "Second bid component"
    
    # Test serialization to dict
    msg_dict = bid_response.model_dump(by_alias=True)
    assert msg_dict["49"] == "SENDER"  # SenderCompID
    assert msg_dict["56"] == "TARGET"  # TargetCompID
    assert msg_dict["390"] == "BID123"  # BidID
    assert msg_dict["391"] == "CLIENT456"  # ClientBidID
    assert msg_dict["420"] == 2  # NoBidComponents
    
    # Test deserialization from dict
    new_bid_response = BidResponse(**msg_dict)
    assert new_bid_response.SenderCompID == "SENDER"
    assert new_bid_response.TargetCompID == "TARGET"
    assert new_bid_response.BidID == "BID123"
    assert new_bid_response.ClientBidID == "CLIENT456"
    assert new_bid_response.NoBidComponents == 2
    assert len(new_bid_response.BidComponents) == 2

def test_bidresponse_validation():
    # Test required fields validation
    with pytest.raises(ValueError):
        BidResponse()  # Should fail as MsgType is required
    
    # Test invalid field values
    with pytest.raises(ValueError):
        BidResponse(
            MsgType="l",
            Side="3"  # Invalid side value (should be 1 or 2)
        )
    
    # Test component validation
    with pytest.raises(ValueError):
        BidResponse(
            MsgType="l",
            NoBidComponents=1,
            BidComponents=[
                BidResponseComponent(
                    Commission=-1.0  # Invalid negative commission
                )
            ]
        ) 