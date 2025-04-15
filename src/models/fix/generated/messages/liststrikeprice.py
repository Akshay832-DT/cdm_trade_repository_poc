"""FIX message model for ListStrikePrice (m).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtstrkpxgrp import InstrmtStrkPxGrpComponent
from ..components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrpComponent

class ListStrikePriceMessage(FIXMessageBase):
    """FIX message model for ListStrikePrice."""

    MsgType: str = Field("m", alias="35")

    ListID: str = Field(..., alias='66', description='')
    TotNoStrikes: int = Field(..., alias='422', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    InstrmtStrkPxGrp: InstrmtStrkPxGrpComponent = Field(..., description='')
    UndInstrmtStrkPxGrp: Optional[UndInstrmtStrkPxGrpComponent] = Field(None, description='')

