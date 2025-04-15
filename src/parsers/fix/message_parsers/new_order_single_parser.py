"""
Parser for NewOrderSingle FIX messages.
"""
from typing import Optional
import simplefix
from datetime import datetime
from src.models.fix.generated.messages.newordersingle import NewOrderSingleMessage
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent

class NewOrderSingleParser:
    """Parser for NewOrderSingle FIX messages."""
    
    async def parse(self, message: simplefix.FixMessage) -> Optional[NewOrderSingleMessage]:
        """
        Parse a NewOrderSingle FIX message.
        
        Args:
            message: The FIX message to parse
            
        Returns:
            The parsed NewOrderSingleMessage or None if parsing fails
        """
        try:
            # Create the message object
            new_order = NewOrderSingleMessage()
            
            # Set basic fields
            new_order.BeginString = message.get(8).decode()
            new_order.MsgType = message.get(35).decode()
            new_order.SenderCompID = message.get(49).decode()
            new_order.TargetCompID = message.get(56).decode()
            new_order.MsgSeqNum = int(message.get(34).decode())
            new_order.SendingTime = datetime.strptime(message.get(52).decode(), "%Y%m%d-%H:%M:%S")
            
            # Set order-specific fields
            new_order.ClOrdID = message.get(11).decode()
            new_order.Account = message.get(1).decode()
            new_order.HandlInst = message.get(21).decode()
            
            # Create and set Instrument component
            instrument = InstrumentComponent()
            instrument.Symbol = message.get(55).decode()
            instrument.SecurityID = message.get(48).decode()
            instrument.SecurityIDSource = message.get(22).decode()
            instrument.SecurityType = message.get(167).decode()
            instrument.MaturityMonthYear = message.get(200).decode()
            instrument.MaturityDate = datetime.strptime(message.get(541).decode(), "%Y%m%d").date()
            instrument.SecurityExchange = message.get(207).decode()
            instrument.Product = int(message.get(460).decode())
            new_order.Instrument = instrument
            
            # Create and set OrderQtyData component
            order_qty = OrderQtyDataComponent()
            order_qty.OrderQty = float(message.get(38).decode())
            new_order.OrderQtyData = order_qty
            
            # Set other fields
            new_order.OrdType = message.get(40).decode()
            new_order.Price = float(message.get(44).decode())
            new_order.Side = message.get(54).decode()
            new_order.TimeInForce = message.get(59).decode()
            new_order.TransactTime = datetime.strptime(message.get(60).decode(), "%Y%m%d-%H:%M:%S")
            new_order.PositionEffect = message.get(77).decode()
            
            return new_order
            
        except (AttributeError, ValueError, KeyError) as e:
            print(f"Error parsing NewOrderSingle message: {e}")
            return None 