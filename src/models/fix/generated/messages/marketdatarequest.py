"""
FIX 4.4 MarketDataRequest Message

This module contains the Pydantic model for the MarketDataRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtmdreqgrp import InstrmtMDReqGrp
from ..components.mdreqgrp import MDReqGrp
from ..components.trdgsesgrp import TrdgSesGrp


class MarketDataRequest(TradeModel):
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
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["V"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    MDReqID: str = Field(None, description='', alias='262')
    SubscriptionRequestType: str = Field(None, description='', alias='263')
    MarketDepth: int = Field(None, description='', alias='264')
    MDUpdateType: Optional[int] = Field(None, description='', alias='265')
    AggregatedBook: Optional[bool] = Field(None, description='', alias='266')
    OpenCloseSettlFlag: Optional[List[str]] = Field(None, description='', alias='286')
    Scope: Optional[List[str]] = Field(None, description='', alias='546')
    MDImplicitDelete: Optional[bool] = Field(None, description='', alias='547')
    ApplQueueAction: Optional[int] = Field(None, description='', alias='815')
    ApplQueueMax: Optional[int] = Field(None, description='', alias='812')
    MDReqGrp: MDReqGrp = Field(..., description='MDReqGrp component')
    InstrmtMDReqGrp: InstrmtMDReqGrp = Field(..., description='InstrmtMDReqGrp component')
    TrdgSesGrp: Optional[TrdgSesGrp] = None

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
