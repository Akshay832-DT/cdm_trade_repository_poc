from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.commissiondata import CommissionData

class NoBidComponents(FIXMessageBase):
    """FIX group model."""

    listID: Optional[str] = Field(None, description='', alias='66')
    country: Optional[str] = Field(None, description='', alias='421')
    side: Optional[str] = Field(None, description='', alias='54')
    price: Optional[str] = Field(None, description='', alias='44')
    priceType: Optional[str] = Field(None, description='', alias='423')
    fairValue: Optional[str] = Field(None, description='', alias='406')
    netGrossInd: Optional[str] = Field(None, description='', alias='430')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[str] = Field(None, description='', alias='64')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[str] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    commissionData: CommissionData = Field(..., description='CommissionData component')

class BidCompRspGrp(FIXMessageBase):
    """FIX component model."""

    noBidComponents: int = Field(..., description='Number of NoBidComponents entries', alias='420')
    noBidComponents_items: List[NoBidComponents] = Field(default_factory=list)

