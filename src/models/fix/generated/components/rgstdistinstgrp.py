"""
FIX 4.4 RgstDistInstGrp Component

This module contains the Pydantic model for the RgstDistInstGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class RgstDistInstGrp(TradeModel):
    """
    FIX 4.4 RgstDistInstGrp Component
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
    DistribPaymentMethod: Optional[int] = Field(None, description='', alias='477')
    DistribPercentage: Optional[float] = Field(None, description='', alias='512')
    CashDistribCurr: Optional[str] = Field(None, description='', alias='478')
    CashDistribAgentName: Optional[str] = Field(None, description='', alias='498')
    CashDistribAgentCode: Optional[str] = Field(None, description='', alias='499')
    CashDistribAgentAcctNumber: Optional[str] = Field(None, description='', alias='500')
    CashDistribPayRef: Optional[str] = Field(None, description='', alias='501')
    CashDistribAgentAcctName: Optional[str] = Field(None, description='', alias='502')


class NoDistribInsts(TradeModel):
    """
    NoDistribInsts group fields
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
    DistribPaymentMethod: Optional[int] = Field(None, description='', alias='477')
    DistribPercentage: Optional[float] = Field(None, description='', alias='512')
    CashDistribCurr: Optional[str] = Field(None, description='', alias='478')
    CashDistribAgentName: Optional[str] = Field(None, description='', alias='498')
    CashDistribAgentCode: Optional[str] = Field(None, description='', alias='499')
    CashDistribAgentAcctNumber: Optional[str] = Field(None, description='', alias='500')
    CashDistribPayRef: Optional[str] = Field(None, description='', alias='501')
    CashDistribAgentAcctName: Optional[str] = Field(None, description='', alias='502')

    NoDistribInstss: List[NoDistribInsts] = Field(default_factory=list)
