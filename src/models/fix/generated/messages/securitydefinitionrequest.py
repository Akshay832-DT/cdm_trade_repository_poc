"""FIX message model for SecurityDefinitionRequest (c).

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

class SecurityDefinitionRequestMessage(FIXMessageBase):
    """FIX message model for SecurityDefinitionRequest."""

    MsgType: str = Field("c", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityRequestType: int = Field(..., alias='321', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    ExpirationCycle: Optional[int] = Field(None, alias='827', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

