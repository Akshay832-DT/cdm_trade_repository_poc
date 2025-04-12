"""
FIX 4.4 MarketDataSnapshotFullRefresh Message

This module contains the Pydantic model for the MarketDataSnapshotFullRefresh message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.mdfullgrp import MDFullGrp
from ..components.undinstrmtgrp import UndInstrmtGrp


class MarketDataSnapshotFullRefresh(TradeModel):
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
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["W"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    MDReqID: Optional[str] = Field(None, description='', alias='262')
    FinancialStatus: Optional[List[str]] = Field(None, description='', alias='291')
    CorporateAction: Optional[List[str]] = Field(None, description='', alias='292')
    NetChgPrevDay: Optional[float] = Field(None, description='', alias='451')
    ApplQueueDepth: Optional[int] = Field(None, description='', alias='813')
    ApplQueueResolution: Optional[int] = Field(None, description='', alias='814')
    Instrument: Instrument = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    MDFullGrp: MDFullGrp = Field(..., description='MDFullGrp component')

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
