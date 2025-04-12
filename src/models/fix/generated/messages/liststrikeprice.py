"""
FIX 4.4 ListStrikePrice Message

This module contains the Pydantic model for the ListStrikePrice message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtstrkpxgrp import InstrmtStrkPxGrp
from src.models.fix.generated.components.undinstrmtstrkpxgrp import UndInstrmtStrkPxGrp


class ListStrikePrice(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["m"] = Field("m", alias='35')
    
    # Message-specific fields
    listID: Optional[str] = Field(None, description='', alias='66')
    totNoStrikes: Optional[int] = Field(None, description='', alias='422')
    lastFragment: Optional[bool] = Field(None, description='', alias='893')
    instrmtStrkPxGrp: Optional[InstrmtStrkPxGrp] = Field(None, description='InstrmtStrkPxGrp component')
    undInstrmtStrkPxGrp: Optional[UndInstrmtStrkPxGrp] = Field(None, description='UndInstrmtStrkPxGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
