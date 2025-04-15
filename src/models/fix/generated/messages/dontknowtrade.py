"""FIX message model for DontKnowTrade (Q).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class DontKnowTradeMessage(FIXMessageBase):
    """FIX message model for DontKnowTrade."""

    MsgType: str = Field("Q", alias="35")

    OrderID: str = Field(..., alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    ExecID: str = Field(..., alias='17', description='')
    DKReason: str = Field(..., alias='127', description='')
    Side: str = Field(..., alias='54', description='')
    LastQty: Optional[float] = Field(None, alias='32', description='')
    LastPx: Optional[float] = Field(None, alias='31', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    OrderQtyData: OrderQtyDataComponent = Field(..., description='')

