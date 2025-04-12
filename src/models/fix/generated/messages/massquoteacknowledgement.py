"""
FIX 4.4 MassQuoteAcknowledgement Message

This module contains the Pydantic model for the MassQuoteAcknowledgement message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.quotsetackgrp import QuotSetAckGrp


class MassQuoteAcknowledgement(FIXMessageBase):
    """
    FIX 4.4 MassQuoteAcknowledgement Message
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
    msgType: Literal["b"] = Field("b", alias='35')
    
    # Message-specific fields
    quoteReqID: Optional[str] = Field(None, description='', alias='131')
    quoteID: Optional[str] = Field(None, description='', alias='117')
    quoteStatus: Optional[int] = Field(None, description='', alias='297')
    quoteRejectReason: Optional[int] = Field(None, description='', alias='300')
    quoteResponseLevel: Optional[int] = Field(None, description='', alias='301')
    quoteType: Optional[int] = Field(None, description='', alias='537')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    quotSetAckGrp: Optional[QuotSetAckGrp] = Field(None, description='QuotSetAckGrp component')

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
