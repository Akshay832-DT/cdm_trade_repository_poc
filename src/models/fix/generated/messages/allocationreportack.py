"""
FIX 4.4 AllocationReportAck Message

This module contains the Pydantic model for the AllocationReportAck message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.allocackgrp import AllocAckGrp
from src.models.fix.generated.components.parties import Parties


class AllocationReportAck(FIXMessageBase):
    """
    FIX 4.4 AllocationReportAck Message
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
    msgType: Literal["AT"] = Field("AT", alias='35')
    
    # Message-specific fields
    allocReportID: Optional[str] = Field(None, description='', alias='755')
    allocID: Optional[str] = Field(None, description='', alias='70')
    secondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    allocStatus: Optional[int] = Field(None, description='', alias='87')
    allocRejCode: Optional[int] = Field(None, description='', alias='88')
    allocReportType: Optional[int] = Field(None, description='', alias='794')
    allocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    matchStatus: Optional[str] = Field(None, description='', alias='573')
    product: Optional[int] = Field(None, description='', alias='460')
    securityType: Optional[str] = Field(None, description='', alias='167')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    allocAckGrp: Optional[AllocAckGrp] = Field(None, description='AllocAckGrp component')

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
