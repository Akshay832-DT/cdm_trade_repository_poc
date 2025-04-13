"""
FIX 4.4 BidCompReqGrp Component

This module contains the Pydantic model for the BidCompReqGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoBidComponentsGroup(FIXComponentBase):
    """
    NoBidComponents group fields
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
    
    ListID: Optional[str] = Field(None, description='', alias='66')
    Side: Optional[str] = Field(None, description='', alias='54')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    NetGrossInd: Optional[int] = Field(None, description='', alias='430')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')


class BidCompReqGrpComponent(FIXComponentBase):
    """
    FIX 4.4 BidCompReqGrp Component
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
    
    NoBidComponents: Optional[int] = Field(None, description='Number of NoBidComponents entries', alias='')
    NoBidComponents_items: List[NoBidComponentsGroup] = Field(default_factory=list)
