"""
FIX 4.4 AssignmentReport Message

This module contains the Pydantic model for the AssignmentReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.positionamountdata import PositionAmountData
from src.models.fix.generated.components.positionqty import PositionQty
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class AssignmentReport(FIXMessageBase):
    """
    FIX 4.4 AssignmentReport Message
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
    msgType: Literal["AW"] = Field("AW", alias='35')
    
    # Message-specific fields
    asgnRptID: Optional[str] = Field(None, description='', alias='833')
    totNumAssignmentReports: Optional[int] = Field(None, description='', alias='832')
    lastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    account: Optional[str] = Field(None, description='', alias='1')
    accountType: Optional[int] = Field(None, description='', alias='581')
    currency: Optional[str] = Field(None, description='', alias='15')
    thresholdAmount: Optional[float] = Field(None, description='', alias='834')
    settlPrice: Optional[float] = Field(None, description='', alias='730')
    settlPriceType: Optional[int] = Field(None, description='', alias='731')
    underlyingSettlPrice: Optional[float] = Field(None, description='', alias='732')
    expireDate: Optional[date] = Field(None, description='', alias='432')
    assignmentMethod: Optional[str] = Field(None, description='', alias='744')
    assignmentUnit: Optional[float] = Field(None, description='', alias='745')
    openInterest: Optional[float] = Field(None, description='', alias='746')
    exerciseMethod: Optional[str] = Field(None, description='', alias='747')
    settlSessID: Optional[str] = Field(None, description='', alias='716')
    settlSessSubID: Optional[str] = Field(None, description='', alias='717')
    clearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    positionQty: Optional[PositionQty] = Field(None, description='PositionQty component')
    positionAmountData: Optional[PositionAmountData] = Field(None, description='PositionAmountData component')

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
