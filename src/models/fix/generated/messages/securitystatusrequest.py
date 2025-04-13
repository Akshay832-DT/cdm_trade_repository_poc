from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrumentextension import InstrumentExtensionComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent

class SecurityStatusRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    SecurityStatusReqID: str = Field(..., description='', alias='324')
    Currency: Optional[str] = Field(None, description='', alias='15')
    SubscriptionRequestType: str = Field(..., description='', alias='263')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='InstrumentExtension component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')

