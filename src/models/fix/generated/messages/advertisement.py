"""
FIX 4.4 Advertisement Message

This module contains the Pydantic model for the Advertisement message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.undinstrmtgrp import UndInstrmtGrp


class Advertisement(TradeModel):
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
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["7"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    AdvId: str = Field(None, description='', alias='2')
    AdvTransType: str = Field(None, description='', alias='5')
    AdvRefID: Optional[str] = Field(None, description='', alias='3')
    AdvSide: str = Field(None, description='', alias='4')
    Quantity: float = Field(None, description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Price: Optional[float] = Field(None, description='', alias='44')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    URLLink: Optional[str] = Field(None, description='', alias='149')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Instrument: Instrument = Field(..., description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None

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
