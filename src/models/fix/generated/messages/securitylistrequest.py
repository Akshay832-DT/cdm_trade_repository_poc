"""FIX message model for SecurityListRequest (x).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.instrumentextension import InstrumentExtensionComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class SecurityListRequestMessage(FIXMessageBase):
    """FIX message model for SecurityListRequest."""

    MsgType: str = Field("x", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityListRequestType: int = Field(..., alias='559', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrumentExtension: Optional[InstrumentExtensionComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')

