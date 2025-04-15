"""FIX message model for SecurityList (y).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.seclistgrp import SecListGrpComponent

class SecurityListMessage(FIXMessageBase):
    """FIX message model for SecurityList."""

    MsgType: str = Field("y", alias="35")

    SecurityReqID: str = Field(..., alias='320', description='')
    SecurityResponseID: str = Field(..., alias='322', description='')
    SecurityRequestResult: int = Field(..., alias='560', description='')
    TotNoRelatedSym: Optional[int] = Field(None, alias='393', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    SecListGrp: Optional[SecListGrpComponent] = Field(None, description='')

