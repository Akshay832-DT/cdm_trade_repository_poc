"""
FIX 4.4 NetworkCounterpartySystemStatusResponse Message

This module contains the Pydantic model for the NetworkCounterpartySystemStatusResponse message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.compidstatgrp import CompIDStatGrp


class NetworkCounterpartySystemStatusResponse(FIXMessageBase):
    """
    FIX 4.4 NetworkCounterpartySystemStatusResponse Message
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
    msgType: Literal["BD"] = Field("BD", alias='35')
    
    # Message-specific fields
    networkStatusResponseType: Optional[int] = Field(None, description='', alias='937')
    networkRequestID: Optional[str] = Field(None, description='', alias='933')
    networkResponseID: Optional[str] = Field(None, description='', alias='932')
    lastNetworkResponseID: Optional[str] = Field(None, description='', alias='934')
    compIDStatGrp: Optional[CompIDStatGrp] = Field(None, description='CompIDStatGrp component')

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
