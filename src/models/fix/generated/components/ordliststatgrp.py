"""
FIX 4.4 OrdListStatGrp Component

This module contains the Pydantic model for the OrdListStatGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoOrdersGroup(FIXComponentBase):
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
    
    ClOrdID: str = Field(..., description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    CumQty: float = Field(..., description='', alias='14')
    OrdStatus: str = Field(..., description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    LeavesQty: float = Field(..., description='', alias='151')
    CxlQty: float = Field(..., description='', alias='84')
    AvgPx: float = Field(..., description='', alias='6')
    OrdRejReason: Optional[int] = Field(None, description='', alias='103')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')


class OrdListStatGrpComponent(FIXComponentBase):
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
    
    NoOrders: Optional[int] = Field(None, description='Number of NoOrders entries', alias='')
    NoOrders_items: List[NoOrdersGroup] = Field(default_factory=list)
