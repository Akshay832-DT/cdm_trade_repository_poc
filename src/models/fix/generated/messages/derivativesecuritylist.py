"""FIX message model for DerivativeSecurityList (AA).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.relsymderivsecgrp import RelSymDerivSecGrpComponent
from ..components.underlyinginstrument import UnderlyingInstrumentComponent

class DerivativeSecurityListMessage(FIXMessageBase):
    """FIX message model for DerivativeSecurityList."""

    MsgType: str = Field("AA", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityResponseID: str = Field(..., alias='322', description='')
    SecurityRequestResult: int = Field(..., alias='560', description='')
    TotNoRelatedSym: Optional[int] = Field(None, alias='393', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    UnderlyingInstrument: Optional[UnderlyingInstrumentComponent] = Field(None, description='')
    RelSymDerivSecGrp: Optional[RelSymDerivSecGrpComponent] = Field(None, description='')

