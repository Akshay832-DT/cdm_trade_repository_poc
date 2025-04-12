"""
FIX 4.4 BidResponse message

This module contains the Pydantic model for the BidResponse message (type: l).
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ..base import FIXMessageBase
from ...base import TradeModel

class BidResponseComponent(TradeModel):
    """BidResponse component"""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    Commission: Optional[float] = Field(None, description="Commission amount", alias='12')
    CommType: Optional[str] = Field(None, description="Commission type (1=Per unit, 2=Percentage, 3=Absolute)", alias='13')
    CommCurrency: Optional[str] = Field(None, description="Currency of commission", alias='479')
    FundRenewWaiv: Optional[str] = Field(None, description="Fund renewal waiver (Y/N)", alias='497')
    ListID: Optional[str] = Field(None, description="List identifier", alias='66')
    Country: Optional[str] = Field(None, description="Country of origin", alias='421')
    Side: Optional[str] = Field(None, description="Side of order (1=Buy, 2=Sell)", alias='54')
    Price: Optional[float] = Field(None, description="Bid price", alias='44')
    PriceType: Optional[int] = Field(None, description="Price type", alias='423')
    FairValue: Optional[float] = Field(None, description="Fair value", alias='406')
    NetGrossInd: Optional[int] = Field(None, description="Net/Gross indicator", alias='430')
    SettlType: Optional[str] = Field(None, description="Settlement type", alias='63')
    SettlDate: Optional[date] = Field(None, description="Settlement date", alias='64')
    TradingSessionID: Optional[str] = Field(None, description="Trading session ID", alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description="Trading session sub ID", alias='625')
    Text: Optional[str] = Field(None, description="Additional text/comments", alias='58')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        return {k: v for k, v in data.items() if v is not None}

class BidResponse(FIXMessageBase):
    """FIX 4.4 BidResponse message"""
    
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field("FIX.4.4", alias='8')
    BodyLength: Optional[int] = Field(None)
    MsgType: Literal["l"] = Field("l", alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    BidID: Optional[str] = Field(None, alias='390')
    ClientBidID: Optional[str] = Field(None, alias='391')
    NoBidComponents: Optional[int] = Field(None, alias='420')
    BidComponents: Optional[List[BidResponseComponent]] = Field(None, description="List of bid components")
    
    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        if self.BidComponents:
            data['420'] = len(self.BidComponents)  # Set NoBidComponents using FIX tag
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
