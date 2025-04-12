"""
FIX 4.4 BidRequest Message

This module contains the Pydantic model for the BidRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.bidcompreqgrp import BidCompReqGrp
from src.models.fix.generated.components.biddescreqgrp import BidDescReqGrp


class BidRequest(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["k"] = Field("k", alias='35')
    
    # Message-specific fields
    bidID: Optional[str] = Field(None, description='', alias='390')
    clientBidID: Optional[str] = Field(None, description='', alias='391')
    bidRequestTransType: Optional[str] = Field(None, description='', alias='374')
    listName: Optional[str] = Field(None, description='', alias='392')
    totNoRelatedSym: Optional[int] = Field(None, description='', alias='393')
    bidType: Optional[int] = Field(None, description='', alias='394')
    numTickets: Optional[int] = Field(None, description='', alias='395')
    currency: Optional[str] = Field(None, description='', alias='15')
    sideValue1: Optional[float] = Field(None, description='', alias='396')
    sideValue2: Optional[float] = Field(None, description='', alias='397')
    liquidityIndType: Optional[int] = Field(None, description='', alias='409')
    wtAverageLiquidity: Optional[float] = Field(None, description='', alias='410')
    exchangeForPhysical: Optional[bool] = Field(None, description='', alias='411')
    outMainCntryUIndex: Optional[float] = Field(None, description='', alias='412')
    crossPercent: Optional[float] = Field(None, description='', alias='413')
    progRptReqs: Optional[int] = Field(None, description='', alias='414')
    progPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    incTaxInd: Optional[int] = Field(None, description='', alias='416')
    forexReq: Optional[bool] = Field(None, description='', alias='121')
    numBidders: Optional[int] = Field(None, description='', alias='417')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    bidTradeType: Optional[str] = Field(None, description='', alias='418')
    basisPxType: Optional[str] = Field(None, description='', alias='419')
    strikeTime: Optional[datetime] = Field(None, description='', alias='443')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    bidDescReqGrp: Optional[BidDescReqGrp] = Field(None, description='BidDescReqGrp component')
    bidCompReqGrp: Optional[BidCompReqGrp] = Field(None, description='BidCompReqGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
