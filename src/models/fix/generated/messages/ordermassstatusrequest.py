"""FIX message model for OrderMassStatusRequest (AF).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.underlyinginstrument import UnderlyingInstrumentComponent

class OrderMassStatusRequestMessage(FIXMessageBase):
    """FIX message model for OrderMassStatusRequest."""

    MsgType: str = Field("AF", alias="35")

    MassStatusReqID: str = Field(..., alias='584', description='')
    MassStatusReqType: int = Field(..., alias='585', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')

