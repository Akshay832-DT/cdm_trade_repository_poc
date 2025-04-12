"""
FIX 4.4 NewOrderList Message

This module contains the Pydantic model for the NewOrderList message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.listordgrp import ListOrdGrp


class NewOrderList(FIXMessageBase):
    """
    FIX 4.4 NewOrderList Message
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
    msgType: Literal["E"] = Field("E", alias='35')
    
    # Message-specific fields
    listID: Optional[str] = Field(None, description='', alias='66')
    bidID: Optional[str] = Field(None, description='', alias='390')
    clientBidID: Optional[str] = Field(None, description='', alias='391')
    progRptReqs: Optional[int] = Field(None, description='', alias='414')
    bidType: Optional[int] = Field(None, description='', alias='394')
    progPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    cancellationRights: Optional[str] = Field(None, description='', alias='480')
    moneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    registID: Optional[str] = Field(None, description='', alias='513')
    listExecInstType: Optional[str] = Field(None, description='', alias='433')
    listExecInst: Optional[str] = Field(None, description='', alias='69')
    encodedListExecInstLen: Optional[int] = Field(None, description='', alias='352')
    encodedListExecInst: Optional[str] = Field(None, description='', alias='353')
    allowableOneSidednessPct: Optional[float] = Field(None, description='', alias='765')
    allowableOneSidednessValue: Optional[float] = Field(None, description='', alias='766')
    allowableOneSidednessCurr: Optional[str] = Field(None, description='', alias='767')
    totNoOrders: Optional[int] = Field(None, description='', alias='68')
    lastFragment: Optional[bool] = Field(None, description='', alias='893')
    listOrdGrp: Optional[ListOrdGrp] = Field(None, description='ListOrdGrp component')

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
