"""
FIX Component Model - SideCrossOrdCxlGrp
"""

from ..base import FIXComponentBase
from .orderqtydata import OrderQtyDataComponent
from .parties import PartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSidesGroup(FIXComponentBase):

    """FIX Group - NoSides"""

    Side: str = Field(alias='54', description='')
    OrigClOrdID: str = Field(alias='41', description='')
    ClOrdID: str = Field(alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    OrigOrdModTime: Optional[datetime] = Field(None, alias='586', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    ComplianceID: Optional[str] = Field(None, alias='376', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    OrderQtyData: OrderQtyDataComponent



class SideCrossOrdCxlGrpComponent(FIXComponentBase):
    """FIX Component - SideCrossOrdCxlGrp"""


