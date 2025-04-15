"""FIX message model for RegistrationInstructionsResponse (p).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent

class RegistrationInstructionsResponseMessage(FIXMessageBase):
    """FIX message model for RegistrationInstructionsResponse."""

    MsgType: str = Field("p", alias="35")

    RegistID: str = Field(..., alias='513', description='')
    RegistTransType: str = Field(..., alias='514', description='')
    RegistRefID: str = Field(..., alias='508', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    RegistStatus: str = Field(..., alias='506', description='')
    RegistRejReasonCode: Optional[int] = Field(None, alias='507', description='')
    RegistRejReasonText: Optional[str] = Field(None, alias='496', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')

