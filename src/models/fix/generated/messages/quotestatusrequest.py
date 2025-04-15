"""FIX message model for QuoteStatusRequest (a).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class QuoteStatusRequestMessage(FIXMessageBase):
    """FIX message model for QuoteStatusRequest."""

    MsgType: str = Field("a", alias="35")

    QuoteStatusReqID: Optional[str] = Field(None, alias='649', description='')
    QuoteID: Optional[str] = Field(None, alias='117', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')

