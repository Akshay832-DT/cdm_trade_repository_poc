"""
FIX 4.4 BidRequest Message

This module contains the Pydantic model for the BidRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.bidcompreqgrp import BidCompReqGrp
from ..components.biddescreqgrp import BidDescReqGrp


class BidRequest(TradeModel):
    """
    FIX 4.4 BidRequest Message
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
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["k"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    BidID: Optional[str] = Field(None, description='', alias='390')
    ClientBidID: str = Field(None, description='', alias='391')
    BidRequestTransType: str = Field(None, description='', alias='374')
    ListName: Optional[str] = Field(None, description='', alias='392')
    TotNoRelatedSym: int = Field(None, description='', alias='393')
    BidType: int = Field(None, description='', alias='394')
    NumTickets: Optional[int] = Field(None, description='', alias='395')
    Currency: Optional[str] = Field(None, description='', alias='15')
    SideValue1: Optional[float] = Field(None, description='', alias='396')
    SideValue2: Optional[float] = Field(None, description='', alias='397')
    LiquidityIndType: Optional[int] = Field(None, description='', alias='409')
    WtAverageLiquidity: Optional[float] = Field(None, description='', alias='410')
    ExchangeForPhysical: Optional[bool] = Field(None, description='', alias='411')
    OutMainCntryUIndex: Optional[float] = Field(None, description='', alias='412')
    CrossPercent: Optional[float] = Field(None, description='', alias='413')
    ProgRptReqs: Optional[int] = Field(None, description='', alias='414')
    ProgPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    IncTaxInd: Optional[int] = Field(None, description='', alias='416')
    ForexReq: Optional[bool] = Field(None, description='', alias='121')
    NumBidders: Optional[int] = Field(None, description='', alias='417')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    BidTradeType: str = Field(None, description='', alias='418')
    BasisPxType: str = Field(None, description='', alias='419')
    StrikeTime: Optional[datetime] = Field(None, description='', alias='443')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    BidDescReqGrp: Optional[BidDescReqGrp] = None
    BidCompReqGrp: Optional[BidCompReqGrp] = None

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"No{field_name[:-1]}"  # Remove 's' from plural
                if no_field in self.__fields__:
                    data[no_field] = len(value)
        
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
