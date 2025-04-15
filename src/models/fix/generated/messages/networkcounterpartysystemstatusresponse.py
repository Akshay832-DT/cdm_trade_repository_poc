"""FIX message model for NetworkCounterpartySystemStatusResponse (BD).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.compidstatgrp import CompIDStatGrpComponent

class NetworkCounterpartySystemStatusResponseMessage(FIXMessageBase):
    """FIX message model for NetworkCounterpartySystemStatusResponse."""

    MsgType: str = Field("BD", alias="35")

    NetworkStatusResponseType: int = Field(..., alias='937', description='')
    NetworkRequestID: Optional[str] = Field(None, alias='933', description='')
    NetworkResponseID: str = Field(..., alias='932', description='')
    LastNetworkResponseID: Optional[str] = Field(None, alias='934', description='')
    CompIDStatGrp: CompIDStatGrpComponent = Field(..., description='')

