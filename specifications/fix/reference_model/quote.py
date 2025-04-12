"""
FIX 4.4 Quote Message

This module contains the Pydantic model for the Quote message (type: S).
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal, ForwardRef
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ..base import FIXMessageBase
from ...base import TradeModel

class Instrument(TradeModel):
    """Instrument component"""
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    Symbol: str = Field(..., alias='55')
    SymbolSfx: Optional[str] = Field(None, alias='65')
    SecurityID: Optional[str] = Field(None, alias='48')
    SecurityIDSource: Optional[str] = Field(None, alias='22')
    SecurityExchange: Optional[str] = Field(None, alias='207')
    SecurityDesc: Optional[str] = Field(None, alias='107')
    SecurityType: Optional[str] = Field(None, alias='167')
    MaturityDate: Optional[date] = Field(None, alias='541')
    CouponRate: Optional[float] = Field(None, alias='223')
    ContractMultiplier: Optional[float] = Field(None, alias='231')
    MinPriceIncrement: Optional[float] = Field(None, alias='969')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        data = super().model_dump(**kwargs)
        return {k: v for k, v in data.items() if v is not None}

class OrderQtyData(TradeModel):
    """Order Quantity Data component"""
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    OrderQty: Optional[float] = Field(None, alias='38')
    CashOrderQty: Optional[float] = Field(None, alias='152')
    OrderPercent: Optional[float] = Field(None, alias='516')
    RoundingDirection: Optional[str] = Field(None, alias='468')
    RoundingModulus: Optional[float] = Field(None, alias='469')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        data = super().model_dump(**kwargs)
        return {k: v for k, v in data.items() if v is not None}

class Quote(FIXMessageBase):
    """
    FIX 4.4 Quote Message (Type: S)
    """
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )

    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field("FIX.4.4", alias='8')
    BodyLength: Optional[int] = Field(None)
    MsgType: Literal["S"] = Field("S", alias='35')
    SenderCompID: str
    TargetCompID: str
    MsgSeqNum: int
    SendingTime: datetime
    
    # Message-specific fields
    QuoteReqID: Optional[str] = Field(None, alias='131')
    QuoteID: str = Field(..., alias='117')
    QuoteRespID: Optional[str] = Field(None, alias='693')
    QuoteType: Optional[int] = Field(None, alias='537')
    NoQuoteQualifiers: Optional[int] = Field(None, alias='735')
    QuoteQualifier: Optional[str] = Field(None, alias='695')
    QuoteResponseLevel: Optional[int] = Field(None, alias='301')
    TradingSessionID: Optional[str] = Field(None, alias='336')
    TradingSessionSubID: Optional[str] = Field(None, alias='625')
    
    # Instrument component
    Instrument: Optional[Instrument] = None
    
    Side: Optional[str] = Field(None, alias='54')
    
    # OrderQtyData component
    OrderQtyData: Optional[OrderQtyData] = None
    
    SettlType: Optional[str] = Field(None, alias='63')
    SettlDate: Optional[date] = Field(None, alias='64')
    SettlDate2: Optional[date] = Field(None, alias='193')
    OrderQty2: Optional[float] = Field(None, alias='192')
    Currency: Optional[str] = Field(None, alias='15')
    
    # Additional quote fields
    BidPx: Optional[float] = Field(None, alias='132')
    OfferPx: Optional[float] = Field(None, alias='133')
    BidSize: Optional[float] = Field(None, alias='134')
    OfferSize: Optional[float] = Field(None, alias='135')
    ValidUntilTime: Optional[datetime] = Field(None, alias='62')
    BidSpotRate: Optional[float] = Field(None, alias='188')
    OfferSpotRate: Optional[float] = Field(None, alias='190')
    BidForwardPoints: Optional[float] = Field(None, alias='189')
    OfferForwardPoints: Optional[float] = Field(None, alias='191')
    TransactTime: Optional[datetime] = Field(None, alias='60')
    Text: Optional[str] = Field(None, alias='58')
    EncodedTextLen: Optional[int] = Field(None, alias='354')
    EncodedText: Optional[str] = Field(None, alias='355')
    Price: Optional[float] = Field(None, alias='44')
    PriceType: Optional[int] = Field(None, alias='423')
    Spread: Optional[float] = Field(None, alias='218')
    BenchmarkCurveCurrency: Optional[str] = Field(None, alias='220')
    BenchmarkCurveName: Optional[str] = Field(None, alias='221')
    BenchmarkCurvePoint: Optional[str] = Field(None, alias='222')
    BenchmarkPrice: Optional[float] = Field(None, alias='662')
    BenchmarkPriceType: Optional[int] = Field(None, alias='663')
    BenchmarkSecurityID: Optional[str] = Field(None, alias='699')
    BenchmarkSecurityIDSource: Optional[str] = Field(None, alias='761')
    YieldType: Optional[str] = Field(None, alias='235')
    Yield: Optional[float] = Field(None, alias='236')
    YieldCalcDate: Optional[date] = Field(None, alias='701')
    YieldRedemptionDate: Optional[date] = Field(None, alias='696')
    YieldRedemptionPrice: Optional[float] = Field(None, alias='697')
    YieldRedemptionPriceType: Optional[int] = Field(None, alias='698')
    BidSwapPoints: Optional[float] = Field(None, alias='1065')
    MidSwapPoints: Optional[float] = Field(None, alias='1066')
    OfferSwapPoints: Optional[float] = Field(None, alias='1067')
    MinBidSize: Optional[float] = Field(None, alias='647')
    MinOfferSize: Optional[float] = Field(None, alias='648')
    MidPx: Optional[float] = Field(None, alias='631')
    BidYield: Optional[float] = Field(None, alias='632')
    MidYield: Optional[float] = Field(None, alias='633')
    OfferYield: Optional[float] = Field(None, alias='634')
    OrdType: Optional[str] = Field(None, alias='40')
    BidForwardPoints2: Optional[float] = Field(None, alias='642')
    OfferForwardPoints2: Optional[float] = Field(None, alias='643')
    SettlCurrBidFxRate: Optional[float] = Field(None, alias='656')
    SettlCurrOfferFxRate: Optional[float] = Field(None, alias='657')
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias='156')
    CommType: Optional[str] = Field(None, alias='13')
    Commission: Optional[float] = Field(None, alias='12')
    CustOrderCapacity: Optional[int] = Field(None, alias='582')
    ExDestination: Optional[str] = Field(None, alias='100')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        data = super().model_dump(**kwargs)
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
