"""
FIX 4.4 RegistrationInstructionsResponse Message

This module contains the Pydantic model for the RegistrationInstructionsResponse message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.parties import Parties


class RegistrationInstructionsResponse(FIXMessageBase):
    """
    FIX 4.4 RegistrationInstructionsResponse Message
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
    msgType: Literal["p"] = Field("p", alias='35')
    
    # Message-specific fields
    registID: Optional[str] = Field(None, description='', alias='513')
    registTransType: Optional[str] = Field(None, description='', alias='514')
    registRefID: Optional[str] = Field(None, description='', alias='508')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    registStatus: Optional[str] = Field(None, description='', alias='506')
    registRejReasonCode: Optional[int] = Field(None, description='', alias='507')
    registRejReasonText: Optional[str] = Field(None, description='', alias='496')
    parties: Optional[Parties] = Field(None, description='Parties component')

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
