"""
FIX 4.4 SideCrossOrdCxlGrp Component

This module contains the Pydantic model for the SideCrossOrdCxlGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel


class SideCrossOrdCxlGrp(TradeModel):
    """
    FIX 4.4 SideCrossOrdCxlGrp Component
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
    Side: str = Field(None, description='', alias='54')
    OrigClOrdID: str = Field(None, description='', alias='41')
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    OrigOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[str] = Field(None)
    OrderQtyData: str = Field(None)


class NoSides(TradeModel):
    """
    NoSides group fields
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
    Side: str = Field(None, description='', alias='54')
    OrigClOrdID: str = Field(None, description='', alias='41')
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    OrigOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')

    NoSidess: List[NoSides] = Field(default_factory=list)
