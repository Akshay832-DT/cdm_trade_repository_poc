"""
FIX 4.4 OrdListStatGrp Component

This module contains the Pydantic model for the OrdListStatGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class OrdListStatGrp(TradeModel):
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
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    CumQty: float = Field(None, description='', alias='14')
    OrdStatus: str = Field(None, description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    LeavesQty: float = Field(None, description='', alias='151')
    CxlQty: float = Field(None, description='', alias='84')
    AvgPx: float = Field(None, description='', alias='6')
    OrdRejReason: Optional[int] = Field(None, description='', alias='103')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')


class NoOrders(TradeModel):
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
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    CumQty: float = Field(None, description='', alias='14')
    OrdStatus: str = Field(None, description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    LeavesQty: float = Field(None, description='', alias='151')
    CxlQty: float = Field(None, description='', alias='84')
    AvgPx: float = Field(None, description='', alias='6')
    OrdRejReason: Optional[int] = Field(None, description='', alias='103')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

    NoOrderss: List[NoOrders] = Field(default_factory=list)
