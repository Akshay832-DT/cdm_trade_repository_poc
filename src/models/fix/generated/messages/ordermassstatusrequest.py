"""
FIX 4.4 OrderMassStatusRequest Message

This module contains the Pydantic model for the OrderMassStatusRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument


class OrderMassStatusRequest(FIXMessageBase):
    """
    FIX 4.4 OrderMassStatusRequest Message
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
    msgType: Literal["AF"] = Field("AF", alias='35')
    
    # Message-specific fields
    massStatusReqID: Optional[str] = Field(None, description='', alias='584')
    massStatusReqType: Optional[int] = Field(None, description='', alias='585')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    underlyingInstrument: Optional[UnderlyingInstrument] = Field(None, description='UnderlyingInstrument component')

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
