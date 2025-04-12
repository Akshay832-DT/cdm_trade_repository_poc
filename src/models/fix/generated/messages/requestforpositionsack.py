"""
FIX 4.4 RequestForPositionsAck Message

This module contains the Pydantic model for the RequestForPositionsAck message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class RequestForPositionsAck(FIXMessageBase):
    """
    FIX 4.4 RequestForPositionsAck Message
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
    msgType: Literal["AO"] = Field("AO", alias='35')
    
    # Message-specific fields
    posMaintRptID: Optional[str] = Field(None, description='', alias='721')
    posReqID: Optional[str] = Field(None, description='', alias='710')
    totalNumPosReports: Optional[int] = Field(None, description='', alias='727')
    unsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    posReqResult: Optional[int] = Field(None, description='', alias='728')
    posReqStatus: Optional[int] = Field(None, description='', alias='729')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    responseTransportType: Optional[int] = Field(None, description='', alias='725')
    responseDestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')

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
