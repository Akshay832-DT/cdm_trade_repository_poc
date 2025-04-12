"""
FIX 4.4 Logon Message

This module contains the Pydantic model for the Logon message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *


class Logon(FIXMessageBase):
    """
    FIX 4.4 Logon Message
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
    msgType: Literal["A"] = Field("A", alias='35')
    
    # Message-specific fields
    encryptMethod: Optional[int] = Field(None, description='', alias='98')
    heartBtInt: Optional[int] = Field(None, description='', alias='108')
    rawDataLength: Optional[int] = Field(None, description='', alias='95')
    rawData: Optional[str] = Field(None, description='', alias='96')
    resetSeqNumFlag: Optional[bool] = Field(None, description='', alias='141')
    nextExpectedMsgSeqNum: Optional[int] = Field(None, description='', alias='789')
    maxMessageSize: Optional[int] = Field(None, description='', alias='383')
    refMsgType: Optional[str] = Field(None, description='', alias='372')
    msgDirection: Optional[str] = Field(None, description='', alias='385')
    testMessageIndicator: Optional[bool] = Field(None, description='', alias='464')
    username: Optional[str] = Field(None, description='', alias='553')
    password: Optional[str] = Field(None, description='', alias='554')
    noMsgTypes: Optional[List[NoMsgTypes]] = Field(default_factory=list, description='NoMsgTypes group')

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
