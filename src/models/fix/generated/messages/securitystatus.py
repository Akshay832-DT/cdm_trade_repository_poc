"""
FIX 4.4 SecurityStatus Message

This module contains the Pydantic model for the SecurityStatus message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class SecurityStatus(FIXMessageBase):
    """
    FIX 4.4 SecurityStatus Message
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
    msgType: Literal["f"] = Field("f", alias='35')
    
    # Message-specific fields
    securityStatusReqID: Optional[str] = Field(None, description='', alias='324')
    currency: Optional[str] = Field(None, description='', alias='15')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    unsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    securityTradingStatus: Optional[int] = Field(None, description='', alias='326')
    financialStatus: Optional[List[str]] = Field(default_factory=list, description='', alias='291')
    corporateAction: Optional[List[str]] = Field(default_factory=list, description='', alias='292')
    haltReasonChar: Optional[str] = Field(None, description='', alias='327')
    inViewOfCommon: Optional[bool] = Field(None, description='', alias='328')
    dueToRelated: Optional[bool] = Field(None, description='', alias='329')
    buyVolume: Optional[float] = Field(None, description='', alias='330')
    sellVolume: Optional[float] = Field(None, description='', alias='331')
    highPx: Optional[float] = Field(None, description='', alias='332')
    lowPx: Optional[float] = Field(None, description='', alias='333')
    lastPx: Optional[float] = Field(None, description='', alias='31')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    adjustment: Optional[int] = Field(None, description='', alias='334')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentExtension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
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
