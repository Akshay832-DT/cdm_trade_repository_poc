"""
Test FIX ExecutionReport message creation and validation.
"""
import pytest
from datetime import datetime, date
from src.models.fix.generated.messages.executionreport import ExecutionReportMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.parties import PartiesComponent, NoPartyIDsGroup
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent

def test_execution_report_message_creation():
    """Test creating an ExecutionReport message with all required components."""
    # Create an Instrument component
    instrument = InstrumentComponent(
        Symbol="AAPL",
        SecurityID="037833100",
        SecurityIDSource="1",  # CUSIP
        SecurityType="CS",     # Common Stock
        MaturityMonthYear="202512",
        MaturityDate=date(2025, 12, 15),
        StrikeCurrency="USD"
    )
    
    # Create OrderQtyData component
    order_qty_data = OrderQtyDataComponent(
        OrderQty=1000
    )
    
    # Create Parties component
    parties = PartiesComponent(
        NoParty=2,
        NoParty_items=[
            NoPartyIDsGroup(
                PartyID="BROKER123",
                PartyIDSource="D",  # Proprietary
                PartyRole=1         # Executing Firm
            ),
            NoPartyIDsGroup(
                PartyID="TRADER456",
                PartyIDSource="D",  # Proprietary
                PartyRole=12        # Executing Trader
            )
        ]
    )
    
    # Create the ExecutionReport message
    exec_report = ExecutionReportMessage(
        # Standard header fields
        BeginString="FIX.4.4",
        BodyLength=0,    # Will be calculated
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now(),
        
        # Required ExecutionReport fields
        OrderID="ORD123",
        ExecID="EXEC456",
        ExecType="0",        # New
        OrdStatus="0",       # New
        Side="1",            # Buy
        LeavesQty=1000,
        CumQty=0,
        AvgPx=0,
        
        # Optional fields
        ClOrdID="CLIENT123",
        Price=150.50,
        OrderQty=1000,
        TimeInForce="0",     # Day
        TransactTime=datetime.now(),
        Text="Sample execution report",
        
        # Components
        Instrument=instrument,
        OrderQtyData=order_qty_data,
        Parties=parties
    )
    
    # Validate the message
    assert exec_report.SenderCompID == "SENDER"
    assert exec_report.TargetCompID == "TARGET"
    assert exec_report.MsgType == "8"  # ExecutionReport message type
    assert exec_report.OrderID == "ORD123"
    assert exec_report.ExecID == "EXEC456"
    assert exec_report.ExecType == "0"
    assert exec_report.OrdStatus == "0"
    assert exec_report.Side == "1"
    assert exec_report.LeavesQty == 1000
    
    # Validate Instrument component
    assert exec_report.Instrument.Symbol == "AAPL"
    assert exec_report.Instrument.SecurityID == "037833100"
    assert exec_report.Instrument.SecurityType == "CS"
    assert exec_report.Instrument.MaturityDate == date(2025, 12, 15)
    
    # Validate OrderQtyData component
    assert exec_report.OrderQtyData.OrderQty == 1000
    
    # Validate Parties component
    assert exec_report.Parties.NoParty == 2
    assert len(exec_report.Parties.NoParty_items) == 2
    assert exec_report.Parties.NoParty_items[0].PartyID == "BROKER123"
    assert exec_report.Parties.NoParty_items[0].PartyRole == 1
    assert exec_report.Parties.NoParty_items[1].PartyID == "TRADER456"
    assert exec_report.Parties.NoParty_items[1].PartyRole == 12
    
    # Test serialization to dict
    msg_dict = exec_report.model_dump(by_alias=True)
    assert msg_dict["49"] == "SENDER"     # SenderCompID
    assert msg_dict["56"] == "TARGET"     # TargetCompID
    assert msg_dict["37"] == "ORD123"     # OrderID
    assert msg_dict["17"] == "EXEC456"    # ExecID
    assert msg_dict["150"] == "0"         # ExecType
    assert msg_dict["39"] == "0"          # OrdStatus
    
    # Test model_dump
    msg_dict = exec_report.model_dump()
    assert msg_dict["SenderCompID"] == "SENDER"
    assert msg_dict["TargetCompID"] == "TARGET"
    assert msg_dict["OrderID"] == "ORD123"
    assert msg_dict["ExecID"] == "EXEC456"
    assert msg_dict["Instrument"]["Symbol"] == "AAPL"
    assert msg_dict["OrderQtyData"]["OrderQty"] == 1000

def test_execution_report_validation():
    """Test ExecutionReport validation with missing required fields."""
    # Test required fields validation
    with pytest.raises(ValueError):
        ExecutionReportMessage()  # Should fail as required fields are missing
    
    # Test with minimal required fields
    exec_report = ExecutionReportMessage(
        BeginString="FIX.4.4",
        BodyLength=0,
        MsgType="8",
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now(),
        OrderID="ORD123",
        ExecID="EXEC456",
        ExecType="0",
        OrdStatus="0",
        Side="1",
        LeavesQty=1000,
        CumQty=0,
        AvgPx=0,
        Instrument=InstrumentComponent(Symbol="AAPL")
    )
    
    # Verify it works with minimal fields
    assert exec_report.OrderID == "ORD123"
    assert exec_report.MsgType == "8" 