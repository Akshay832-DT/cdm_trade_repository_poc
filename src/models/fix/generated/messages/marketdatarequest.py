"""
FIX 4.4 MarketDataRequest Message

This module contains the Pydantic model for the MarketDataRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtmdreqgrp import InstrmtMDReqGrp
from src.models.fix.generated.components.mdreqgrp import MDReqGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp


class MarketDataRequest(FIXMessageBase):
    """
    FIX 4.4 MarketDataRequest Message
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
    msgType: Literal["V"] = Field("V", alias='35')
    
    # Message-specific fields
    mDReqID: Optional[str] = Field(None, description='', alias='262')
    subscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    marketDepth: Optional[int] = Field(None, description='', alias='264')
    mDUpdateType: Optional[int] = Field(None, description='', alias='265')
    aggregatedBook: Optional[bool] = Field(None, description='', alias='266')
    openCloseSettlFlag: Optional[List[str]] = Field(default_factory=list, description='', alias='286')
    scope: Optional[List[str]] = Field(default_factory=list, description='', alias='546')
    mDImplicitDelete: Optional[bool] = Field(None, description='', alias='547')
    applQueueAction: Optional[int] = Field(None, description='', alias='815')
    applQueueMax: Optional[int] = Field(None, description='', alias='812')
    mDReqGrp: Optional[MDReqGrp] = Field(None, description='MDReqGrp component')
    instrmtMDReqGrp: Optional[InstrmtMDReqGrp] = Field(None, description='InstrmtMDReqGrp component')
    trdgSesGrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')

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
