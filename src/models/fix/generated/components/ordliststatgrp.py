"""
FIX 4.4 OrdListStatGrp Component

This module contains the Pydantic model for the OrdListStatGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class OrdListStatGrp(FIXMessageBase):
    """
    FIX 4.4 OrdListStatGrp Component
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
    clOrdID: str = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    cumQty: float = Field(None, description='', alias='14')
    ordStatus: str = Field(None, description='', alias='39')
    workingIndicator: Optional[bool] = Field(None, description='', alias='636')
    leavesQty: float = Field(None, description='', alias='151')
    cxlQty: float = Field(None, description='', alias='84')
    avgPx: float = Field(None, description='', alias='6')
    ordRejReason: Optional[int] = Field(None, description='', alias='103')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')


class NoOrders(FIXMessageBase):
    """
    NoOrders group fields
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
    clOrdID: int = Field(None, description='', alias='73')
    secondaryClOrdID: Optional[int] = Field(None, description='', alias='73')
    cumQty: int = Field(None, description='', alias='73')
    ordStatus: int = Field(None, description='', alias='73')
    workingIndicator: Optional[int] = Field(None, description='', alias='73')
    leavesQty: int = Field(None, description='', alias='73')
    cxlQty: int = Field(None, description='', alias='73')
    avgPx: int = Field(None, description='', alias='73')
    ordRejReason: Optional[int] = Field(None, description='', alias='73')
    text: Optional[int] = Field(None, description='', alias='73')
    encodedTextLen: Optional[int] = Field(None, description='', alias='73')
    encodedText: Optional[int] = Field(None, description='', alias='73')

    noOrderss: List[NoOrders] = Field(default_factory=list)
