from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.sidecrossordcxlgrp import SideCrossOrdCxlGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent

class CrossOrderCancelRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    CrossID: str = Field(..., description='', alias='548')
    OrigCrossID: str = Field(..., description='', alias='551')
    CrossType: int = Field(..., description='', alias='549')
    CrossPrioritization: int = Field(..., description='', alias='550')
    TransactTime: datetime = Field(..., description='', alias='60')
    SideCrossOrdCxlGrp: SideCrossOrdCxlGrpComponent = Field(..., description='SideCrossOrdCxlGrp component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')

