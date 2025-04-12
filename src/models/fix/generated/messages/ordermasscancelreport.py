"""
FIX 4.4 OrderMassCancelReport Message

This module contains the Pydantic model for the OrderMassCancelReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.affectedordgrp import AffectedOrdGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.underlyinginstrument import UnderlyingInstrument


class OrderMassCancelReport(FIXMessageBase):
    """
    FIX 4.4 OrderMassCancelReport Message
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
    msgType: Literal["r"] = Field("r", alias='35')
    
    # Message-specific fields
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    orderID: Optional[str] = Field(None, description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    massCancelRequestType: Optional[str] = Field(None, description='', alias='530')
    massCancelResponse: Optional[str] = Field(None, description='', alias='531')
    massCancelRejectReason: Optional[str] = Field(None, description='', alias='532')
    totalAffectedOrders: Optional[int] = Field(None, description='', alias='533')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    side: Optional[str] = Field(None, description='', alias='54')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    affectedOrdGrp: Optional[AffectedOrdGrp] = Field(None, description='AffectedOrdGrp component')
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
