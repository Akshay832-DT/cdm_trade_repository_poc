"""
FIX 4.4 AllocationReport Message

This module contains the Pydantic model for the AllocationReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.allocgrp import AllocGrp
from ..components.execallocgrp import ExecAllocGrp
from ..components.financingdetails import FinancingDetails
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.instrumentextension import InstrumentExtension
from ..components.ordallocgrp import OrdAllocGrp
from ..components.parties import Parties
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class AllocationReport(TradeModel):
    """
    FIX 4.4 AllocationReport Message
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
    MsgType: Literal["AS"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    AllocReportID: str = Field(None, description='', alias='755')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    AllocTransType: str = Field(None, description='', alias='71')
    AllocReportRefID: Optional[str] = Field(None, description='', alias='795')
    AllocCancReplaceReason: Optional[int] = Field(None, description='', alias='796')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    AllocReportType: int = Field(None, description='', alias='794')
    AllocStatus: int = Field(None, description='', alias='87')
    AllocRejCode: Optional[int] = Field(None, description='', alias='88')
    RefAllocID: Optional[str] = Field(None, description='', alias='72')
    AllocIntermedReqType: Optional[int] = Field(None, description='', alias='808')
    AllocLinkID: Optional[str] = Field(None, description='', alias='196')
    AllocLinkType: Optional[int] = Field(None, description='', alias='197')
    BookingRefID: Optional[str] = Field(None, description='', alias='466')
    AllocNoOrdersType: int = Field(None, description='', alias='857')
    PreviouslyReported: Optional[bool] = Field(None, description='', alias='570')
    ReversalIndicator: Optional[bool] = Field(None, description='', alias='700')
    MatchType: Optional[str] = Field(None, description='', alias='574')
    Side: str = Field(None, description='', alias='54')
    Quantity: float = Field(None, description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AvgPx: float = Field(None, description='', alias='6')
    AvgParPx: Optional[float] = Field(None, description='', alias='860')
    Currency: Optional[str] = Field(None, description='', alias='15')
    AvgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    TradeDate: date = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    GrossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    Concession: Optional[float] = Field(None, description='', alias='238')
    TotalTakedown: Optional[float] = Field(None, description='', alias='237')
    NetMoney: Optional[float] = Field(None, description='', alias='118')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    AutoAcceptIndicator: Optional[bool] = Field(None, description='', alias='754')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    NumDaysInterest: Optional[int] = Field(None, description='', alias='157')
    AccruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    TotalAccruedInterestAmt: Optional[float] = Field(None, description='', alias='540')
    InterestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    LegalConfirm: Optional[bool] = Field(None, description='', alias='650')
    TotNoAllocs: Optional[int] = Field(None, description='', alias='892')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    OrdAllocGrp: Optional[OrdAllocGrp] = None
    ExecAllocGrp: Optional[ExecAllocGrp] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtension] = None
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    Parties: Optional[Parties] = None
    Stipulations: Optional[Stipulations] = None
    YieldData: Optional[YieldData] = None
    AllocGrp: Optional[AllocGrp] = None

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
