"""
FIX 4.4 CrossOrderCancelRequest Message

This module contains the Pydantic model for the CrossOrderCancelRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.sidecrossordcxlgrp import SideCrossOrdCxlGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class CrossOrderCancelRequest(FIXMessageBase):
    """
    FIX 4.4 CrossOrderCancelRequest Message
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
    msgType: Literal["u"] = Field("u", alias='35')
    
    # Message-specific fields
    orderID: Optional[str] = Field(None, description='', alias='37')
    crossID: Optional[str] = Field(None, description='', alias='548')
    origCrossID: Optional[str] = Field(None, description='', alias='551')
    crossType: Optional[int] = Field(None, description='', alias='549')
    crossPrioritization: Optional[int] = Field(None, description='', alias='550')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    sideCrossOrdCxlGrp: Optional[SideCrossOrdCxlGrp] = Field(None, description='SideCrossOrdCxlGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')

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
