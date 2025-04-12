"""
FIX 4.4 ConfirmationRequest Message

This module contains the Pydantic model for the ConfirmationRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.ordallocgrp import OrdAllocGrp


class ConfirmationRequest(FIXMessageBase):
    """
    FIX 4.4 ConfirmationRequest Message
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
    msgType: Literal["BH"] = Field("BH", alias='35')
    
    # Message-specific fields
    confirmReqID: Optional[str] = Field(None, description='', alias='859')
    confirmType: Optional[int] = Field(None, description='', alias='773')
    allocID: Optional[str] = Field(None, description='', alias='70')
    secondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    individualAllocID: Optional[str] = Field(None, description='', alias='467')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    allocAccountType: Optional[int] = Field(None, description='', alias='798')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    ordAllocGrp: Optional[OrdAllocGrp] = Field(None, description='OrdAllocGrp component')

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
