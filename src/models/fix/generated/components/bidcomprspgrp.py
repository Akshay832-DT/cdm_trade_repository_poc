from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.commissiondata import CommissionData

class NoBidComponents(FIXMessageBase):
    """FIX group model."""

    listID: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
    side: Optional[str] = Field(None)
    price: Optional[str] = Field(None)
    priceType: Optional[str] = Field(None)
    fairValue: Optional[str] = Field(None)
    netGrossInd: Optional[str] = Field(None)
    settlType: Optional[str] = Field(None)
    settlDate: Optional[str] = Field(None)
    tradingSessionID: Optional[str] = Field(None)
    tradingSessionSubID: Optional[str] = Field(None)
    text: Optional[str] = Field(None)
    encodedTextLen: Optional[str] = Field(None)
    encodedText: Optional[str] = Field(None)

class BidCompRspGrp(FIXMessageBase):
    """FIX component model."""

    commissionData: CommissionData = Field(..., description='CommissionData component')
    noBidComponents: Optional[int] = Field(None, description='Number of NoBidComponents entries', alias='420')
    noBidComponents_items: List[NoBidComponents] = Field(default_factory=list)

