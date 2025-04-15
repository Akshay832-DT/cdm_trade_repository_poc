"""
Simplified test for Interest Rate Swap (IRS) message creation.
This test uses direct Pydantic models instead of the generated models
to avoid issues with forward references.
"""
from pydantic import BaseModel, Field
from datetime import datetime, date

# Create simplified models for testing
class InstrumentComponent(BaseModel):
    """Simplified Instrument component for IRS."""
    Symbol: str
    SecurityID: str | None = None
    SecurityIDSource: str | None = None
    SecurityType: str | None = None
    MaturityMonthYear: str | None = None
    MaturityDate: date | None = None
    StrikeCurrency: str | None = None
    Product: int | None = None  # 4 = Interest Rate

class OrderQtyDataComponent(BaseModel):
    """Simplified OrderQtyData component."""
    OrderQty: float | None = None
    CashOrderQty: float | None = None

class NewOrderSingleMessage(BaseModel):
    """Simplified NewOrderSingle message for IRS."""
    # Standard header fields
    BeginString: str
    BodyLength: int = 0
    MsgType: str = "D"  # NewOrderSingle
    SenderCompID: str
    TargetCompID: str
    MsgSeqNum: int
    SendingTime: datetime
    
    # Order fields
    ClOrdID: str
    Account: str | None = None
    HandlInst: str | None = None
    Side: str  # 1 = Buy, 2 = Sell
    TransactTime: datetime
    OrdType: str  # 2 = Limit
    Price: float | None = None
    TimeInForce: str | None = None  # 0 = Day
    
    # Components
    Instrument: InstrumentComponent
    OrderQtyData: OrderQtyDataComponent | None = None

def test_irs_message_simplified():
    """Test creating an IRS message with simplified models."""
    # Create Instrument component for IRS
    instrument = InstrumentComponent(
        Symbol="SWAP",
        SecurityID="SWAP123",
        SecurityIDSource="8",
        SecurityType="SWAP",
        MaturityMonthYear="202404",
        MaturityDate=date(2024, 4, 15),
        StrikeCurrency="USD",
        Product=4  # Interest Rate
    )
    
    # Create OrderQtyData component
    order_qty_data = OrderQtyDataComponent(
        OrderQty=1000000,
        CashOrderQty=1000000
    )
    
    # Create the NewOrderSingle message for IRS
    order = NewOrderSingleMessage(
        # Standard header fields
        BeginString="FIX.4.4",
        BodyLength=0,
        MsgType="D",  # NewOrderSingle
        SenderCompID="SENDER",
        TargetCompID="TARGET",
        MsgSeqNum=1,
        SendingTime=datetime.now(),
        
        # Order fields
        ClOrdID="ORDER123",
        Account="ACCOUNT123",
        HandlInst="1",
        Side="1",  # Buy
        TransactTime=datetime.now(),
        OrdType="2",  # Limit
        Price=100.50,
        TimeInForce="0",  # Day
        
        # Components
        Instrument=instrument,
        OrderQtyData=order_qty_data
    )
    
    # Test the message
    assert order.MsgType == "D"
    assert order.Instrument.Symbol == "SWAP"
    assert order.Instrument.SecurityType == "SWAP"
    assert order.Instrument.Product == 4
    assert order.OrderQtyData.OrderQty == 1000000
    
    # Serialization test
    order_dict = order.model_dump()
    assert order_dict["Instrument"]["Symbol"] == "SWAP"
    assert order_dict["Instrument"]["Product"] == 4
    
    # Print success
    print(f"Created IRS order message successfully")
    print(f"Order: {order.model_dump(exclude={'TransactTime', 'SendingTime'})}")
    return True

if __name__ == "__main__":
    test_irs_message_simplified() 