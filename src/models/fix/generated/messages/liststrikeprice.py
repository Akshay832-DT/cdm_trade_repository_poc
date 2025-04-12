"""
FIX 4.4 ListStrikePrice Message

This module contains the Pydantic model for the ListStrikePrice message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtstrkpxgrp import InstrmtStrkPxGrp
from ..components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrp


class ListStrikePrice(TradeModel):
    """
    FIX 4.4 ListStrikePrice Message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["m"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    ListID: str = Field(None, description='', alias='66')
    TotNoStrikes: int = Field(None, description='', alias='422')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    InstrmtStrkPxGrp: InstrmtStrkPxGrp = Field(..., description='InstrmtStrkPxGrp component')
    UndInstrmtStrkPxGrp: Optional[UndInstrmtStrkPxGrp] = None

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"No{field_name[:-1]}"  # Remove 's' from plural
                if no_field in self.__fields__:
                    data[no_field] = len(value)
        
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
