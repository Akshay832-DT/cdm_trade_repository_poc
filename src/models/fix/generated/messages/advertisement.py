"""
FIX 4.4 Advertisement Message

This module contains the Pydantic model for the Advertisement message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class Advertisement(FIXMessageBase):
    """
    FIX 4.4 Advertisement Message
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
    msgType: Literal["7"] = Field("7", alias='35')
    
    # Message-specific fields
    advId: Optional[str] = Field(None, description='', alias='2')
    advTransType: Optional[str] = Field(None, description='', alias='5')
    advRefID: Optional[str] = Field(None, description='', alias='3')
    advSide: Optional[str] = Field(None, description='', alias='4')
    quantity: Optional[float] = Field(None, description='', alias='53')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    price: Optional[float] = Field(None, description='', alias='44')
    currency: Optional[str] = Field(None, description='', alias='15')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    uRLLink: Optional[str] = Field(None, description='', alias='149')
    lastMkt: Optional[str] = Field(None, description='', alias='30')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')

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
