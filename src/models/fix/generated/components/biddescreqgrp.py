"""
FIX Component Model - BidDescReqGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoBidDescriptorsGroup(FIXComponentBase):

    """FIX Group - NoBidDescriptors"""

    BidDescriptorType: Optional[int] = Field(None, alias='399', description='')
    BidDescriptor: Optional[str] = Field(None, alias='400', description='')
    SideValueInd: Optional[int] = Field(None, alias='401', description='')
    LiquidityValue: Optional[float] = Field(None, alias='404', description='')
    LiquidityNumSecurities: Optional[int] = Field(None, alias='441', description='')
    LiquidityPctLow: Optional[float] = Field(None, alias='402', description='')
    LiquidityPctHigh: Optional[float] = Field(None, alias='403', description='')
    EFPTrackingError: Optional[float] = Field(None, alias='405', description='')
    FairValue: Optional[float] = Field(None, alias='406', description='')
    OutsideIndexPct: Optional[float] = Field(None, alias='407', description='')
    ValueOfFutures: Optional[float] = Field(None, alias='408', description='')



class BidDescReqGrpComponent(FIXComponentBase):
    """FIX Component - BidDescReqGrp"""


