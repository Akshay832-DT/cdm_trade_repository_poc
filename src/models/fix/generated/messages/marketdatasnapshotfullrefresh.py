"""
FIX 4.4 MarketDataSnapshotFullRefresh Message

This module contains the Pydantic model for the MarketDataSnapshotFullRefresh message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.mdfullgrp import MDFullGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class MarketDataSnapshotFullRefresh(FIXMessageBase):
    """
    FIX 4.4 MarketDataSnapshotFullRefresh Message
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
    msgType: Literal["W"] = Field("W", alias='35')
    
    # Message-specific fields
    mDReqID: Optional[str] = Field(None, description='', alias='262')
    financialStatus: Optional[List[str]] = Field(default_factory=list, description='', alias='291')
    corporateAction: Optional[List[str]] = Field(default_factory=list, description='', alias='292')
    netChgPrevDay: Optional[float] = Field(None, description='', alias='451')
    applQueueDepth: Optional[int] = Field(None, description='', alias='813')
    applQueueResolution: Optional[int] = Field(None, description='', alias='814')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    mDFullGrp: Optional[MDFullGrp] = Field(None, description='MDFullGrp component')

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
