"""FIX message model for SecurityStatusRequest (e).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class SecurityStatusRequestMessage(FIXMessageBase):
    """FIX message model for SecurityStatusRequest."""

    MsgType: str = Field("e", alias="35")

    SecurityStatusReqID: str = Field(..., alias='324', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    SubscriptionRequestType: str = Field(..., alias='263', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

