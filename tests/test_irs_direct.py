"""
Direct test for Interest Rate Swap (IRS) message creation.
"""
import pytest
from datetime import datetime, date

def test_irs_message_direct():
    """
    Test creating an IRS message directly.
    
    Note: We use try/except to provide helpful diagnostics
    for what models are actually available.
    """
    try:
        # Import directly from the generated module
        from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage
        from src.models.fix.generated.components.instrument import InstrumentComponent
        from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
        
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
            SendingTime=datetime.now().strftime("%Y%m%d-%H:%M:%S"),
            CheckSum="123",
            
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
        
        # Print success
        print(f"Created IRS order message successfully: {order}")
        return True
        
    except ImportError as e:
        pytest.fail(f"Import error: {e}")
    except Exception as e:
        pytest.fail(f"Error creating IRS message: {e}")

if __name__ == "__main__":
    test_irs_message_direct() 