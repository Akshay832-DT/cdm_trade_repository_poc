"""
FIX BidRequest Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.bidcompreqgrp import BidCompReqGrpComponent
    from ..components.biddescreqgrp import BidDescReqGrpComponent


# Forward references for components to avoid circular imports
BidCompReqGrpComponent = ForwardRef('BidCompReqGrpComponent')
BidDescReqGrpComponent = ForwardRef('BidDescReqGrpComponent')


class BidRequestMessage(FIXMessageBase):
    """BidRequest Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["BidRequest"] = Field("BidRequest", alias="35", description="Message Type")

    BidID: Optional[str] = Field(None, alias="390", description="")
    ClientBidID: Optional[str] = Field(None, alias="391", description="")
    BidRequestTransType: Optional[str] = Field(None, alias="374", description="")
    ListName: Optional[str] = Field(None, alias="392", description="")
    TotNoRelatedSym: Optional[int] = Field(None, alias="393", description="")
    BidType: Optional[int] = Field(None, alias="394", description="")
    NumTickets: Optional[int] = Field(None, alias="395", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    SideValue1: Optional[float] = Field(None, alias="396", description="")
    SideValue2: Optional[float] = Field(None, alias="397", description="")
    LiquidityIndType: Optional[int] = Field(None, alias="409", description="")
    WtAverageLiquidity: Optional[float] = Field(None, alias="410", description="")
    ExchangeForPhysical: Optional[bool] = Field(None, alias="411", description="")
    OutMainCntryUIndex: Optional[float] = Field(None, alias="412", description="")
    CrossPercent: Optional[float] = Field(None, alias="413", description="")
    ProgRptReqs: Optional[int] = Field(None, alias="414", description="")
    ProgPeriodInterval: Optional[int] = Field(None, alias="415", description="")
    IncTaxInd: Optional[int] = Field(None, alias="416", description="")
    ForexReq: Optional[bool] = Field(None, alias="121", description="")
    NumBidders: Optional[int] = Field(None, alias="417", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    BidTradeType: Optional[str] = Field(None, alias="418", description="")
    BasisPxType: Optional[str] = Field(None, alias="419", description="")
    StrikeTime: Optional[datetime] = Field(None, alias="443", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    BidDescReqGrp: ForwardRef('BidDescReqGrpComponent') = Field(None, description="BidDescReqGrp Component")
    BidCompReqGrp: ForwardRef('BidCompReqGrpComponent') = Field(None, description="BidCompReqGrp Component")

    @model_validator(mode='after')
    def resolve_forward_refs(self) -> 'FIXMessageBase':
        """Resolve forward references."""
        for field_name, field_value in self.model_fields.items():
            if isinstance(field_value.annotation, ForwardRef):
                field_value.annotation = eval(field_value.annotation.__forward_arg__)
        return self

    def __str__(self) -> str:
        fields = []
        if self.MsgType is not None:
            fields.append(f"MsgType={self.MsgType}")
        if self.BidID is not None:
            fields.append(f"BidID={self.BidID}")
        if self.ClientBidID is not None:
            fields.append(f"ClientBidID={self.ClientBidID}")
        if self.BidRequestTransType is not None:
            fields.append(f"BidRequestTransType={self.BidRequestTransType}")
        if self.ListName is not None:
            fields.append(f"ListName={self.ListName}")
        if self.TotNoRelatedSym is not None:
            fields.append(f"TotNoRelatedSym={self.TotNoRelatedSym}")
        if self.BidType is not None:
            fields.append(f"BidType={self.BidType}")
        if self.NumTickets is not None:
            fields.append(f"NumTickets={self.NumTickets}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.SideValue1 is not None:
            fields.append(f"SideValue1={self.SideValue1}")
        if self.SideValue2 is not None:
            fields.append(f"SideValue2={self.SideValue2}")
        if self.LiquidityIndType is not None:
            fields.append(f"LiquidityIndType={self.LiquidityIndType}")
        if self.WtAverageLiquidity is not None:
            fields.append(f"WtAverageLiquidity={self.WtAverageLiquidity}")
        if self.ExchangeForPhysical is not None:
            fields.append(f"ExchangeForPhysical={self.ExchangeForPhysical}")
        if self.OutMainCntryUIndex is not None:
            fields.append(f"OutMainCntryUIndex={self.OutMainCntryUIndex}")
        if self.CrossPercent is not None:
            fields.append(f"CrossPercent={self.CrossPercent}")
        if self.ProgRptReqs is not None:
            fields.append(f"ProgRptReqs={self.ProgRptReqs}")
        if self.ProgPeriodInterval is not None:
            fields.append(f"ProgPeriodInterval={self.ProgPeriodInterval}")
        if self.IncTaxInd is not None:
            fields.append(f"IncTaxInd={self.IncTaxInd}")
        if self.ForexReq is not None:
            fields.append(f"ForexReq={self.ForexReq}")
        if self.NumBidders is not None:
            fields.append(f"NumBidders={self.NumBidders}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.BidTradeType is not None:
            fields.append(f"BidTradeType={self.BidTradeType}")
        if self.BasisPxType is not None:
            fields.append(f"BasisPxType={self.BasisPxType}")
        if self.StrikeTime is not None:
            fields.append(f"StrikeTime={self.StrikeTime}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.BidDescReqGrp is not None:
            fields.append(f"BidDescReqGrp={self.BidDescReqGrp}")
        if self.BidCompReqGrp is not None:
            fields.append(f"BidCompReqGrp={self.BidCompReqGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
BidRequestMessage.model_rebuild()
