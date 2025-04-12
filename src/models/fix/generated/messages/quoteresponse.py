"""
FIX 4.4 QuoteResponse Message

This module contains the Pydantic model for the QuoteResponse message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.financingdetails import FinancingDetails
from ..components.instrument import Instrument
from ..components.legquotgrp import LegQuotGrp
from ..components.orderqtydata import OrderQtyData
from ..components.parties import Parties
from ..components.quotqualgrp import QuotQualGrp
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class QuoteResponse(TradeModel):
    """
    FIX 4.4 QuoteResponse Message
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
    MsgType: Literal["AJ"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    QuoteRespID: str = Field(None, description='', alias='693')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    QuoteRespType: int = Field(None, description='', alias='694')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    IOIID: Optional[str] = Field(None, description='', alias='23')
    QuoteType: Optional[int] = Field(None, description='', alias='537')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    Side: Optional[str] = Field(None, description='', alias='54')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    Currency: Optional[str] = Field(None, description='', alias='15')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    BidPx: Optional[float] = Field(None, description='', alias='132')
    OfferPx: Optional[float] = Field(None, description='', alias='133')
    MktBidPx: Optional[float] = Field(None, description='', alias='645')
    MktOfferPx: Optional[float] = Field(None, description='', alias='646')
    MinBidSize: Optional[float] = Field(None, description='', alias='647')
    BidSize: Optional[float] = Field(None, description='', alias='134')
    MinOfferSize: Optional[float] = Field(None, description='', alias='648')
    OfferSize: Optional[float] = Field(None, description='', alias='135')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    BidSpotRate: Optional[float] = Field(None, description='', alias='188')
    OfferSpotRate: Optional[float] = Field(None, description='', alias='190')
    BidForwardPoints: Optional[float] = Field(None, description='', alias='189')
    OfferForwardPoints: Optional[float] = Field(None, description='', alias='191')
    MidPx: Optional[float] = Field(None, description='', alias='631')
    BidYield: Optional[float] = Field(None, description='', alias='632')
    MidYield: Optional[float] = Field(None, description='', alias='633')
    OfferYield: Optional[float] = Field(None, description='', alias='634')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    BidForwardPoints2: Optional[float] = Field(None, description='', alias='642')
    OfferForwardPoints2: Optional[float] = Field(None, description='', alias='643')
    SettlCurrBidFxRate: Optional[float] = Field(None, description='', alias='656')
    SettlCurrOfferFxRate: Optional[float] = Field(None, description='', alias='657')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    Commission: Optional[float] = Field(None, description='', alias='12')
    CommType: Optional[str] = Field(None, description='', alias='13')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ExDestination: Optional[str] = Field(None, description='', alias='100')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Price: Optional[float] = Field(None, description='', alias='44')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    QuotQualGrp: Optional[QuotQualGrp] = None
    Parties: Optional[Parties] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    OrderQtyData: Optional[OrderQtyData] = None
    Stipulations: Optional[Stipulations] = None
    LegQuotGrp: Optional[LegQuotGrp] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    YieldData: Optional[YieldData] = None

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
