from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent

class DontKnowTrade(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    OrderID: str = Field(..., description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    ExecID: str = Field(..., description='', alias='17')
    DKReason: str = Field(..., description='', alias='127')
    Side: str = Field(..., description='', alias='54')
    LastQty: Optional[float] = Field(None, description='', alias='32')
    LastPx: Optional[float] = Field(None, description='', alias='31')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    OrderQtyData: OrderQtyDataComponent = Field(..., description='OrderQtyData component')

