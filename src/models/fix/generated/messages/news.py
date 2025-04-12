"""
FIX 4.4 News Message

This module contains the Pydantic model for the News message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtgrp import InstrmtGrp
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.linesoftextgrp import LinesOfTextGrp
from src.models.fix.generated.components.routinggrp import RoutingGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class News(FIXMessageBase):
    """
    FIX 4.4 News Message
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
    msgType: Literal["B"] = Field("B", alias='35')
    
    # Message-specific fields
    origTime: Optional[datetime] = Field(None, description='', alias='42')
    urgency: Optional[str] = Field(None, description='', alias='61')
    headline: Optional[str] = Field(None, description='', alias='148')
    encodedHeadlineLen: Optional[int] = Field(None, description='', alias='358')
    encodedHeadline: Optional[str] = Field(None, description='', alias='359')
    uRLLink: Optional[str] = Field(None, description='', alias='149')
    rawDataLength: Optional[int] = Field(None, description='', alias='95')
    rawData: Optional[str] = Field(None, description='', alias='96')
    routingGrp: Optional[RoutingGrp] = Field(None, description='RoutingGrp component')
    instrmtGrp: Optional[InstrmtGrp] = Field(None, description='InstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    linesOfTextGrp: Optional[LinesOfTextGrp] = Field(None, description='LinesOfTextGrp component')

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
