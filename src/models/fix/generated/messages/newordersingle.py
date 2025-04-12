"""
FIX 4.4 NewOrderSingle Message

This module contains the Pydantic model for the NewOrderSingle message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.commissiondata import CommissionData
from ..components.discretioninstructions import DiscretionInstructions
from ..components.financingdetails import FinancingDetails
from ..components.instrument import Instrument
from ..components.orderqtydata import OrderQtyData
from ..components.parties import Parties
from ..components.peginstructions import PegInstructions
from ..components.preallocgrp import PreAllocGrp
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.trdgsesgrp import TrdgSesGrp
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class NewOrderSingle(TradeModel):
    """
    FIX 4.4 NewOrderSingle Message
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
    MsgType: Literal["D"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    ClOrdID: str = Field(None, description='', alias='11')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    DayBookingInst: Optional[str] = Field(None, description='', alias='589')
    BookingUnit: Optional[str] = Field(None, description='', alias='590')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    CashMargin: Optional[str] = Field(None, description='', alias='544')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    HandlInst: Optional[str] = Field(None, description='', alias='21')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    MinQty: Optional[float] = Field(None, description='', alias='110')
    MaxFloor: Optional[float] = Field(None, description='', alias='111')
    ExDestination: Optional[str] = Field(None, description='', alias='100')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    Side: str = Field(None, description='', alias='54')
    LocateReqd: Optional[bool] = Field(None, description='', alias='114')
    TransactTime: datetime = Field(None, description='', alias='60')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    OrdType: str = Field(None, description='', alias='40')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    StopPx: Optional[float] = Field(None, description='', alias='99')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    SolicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    IOIID: Optional[str] = Field(None, description='', alias='23')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    TimeInForce: Optional[str] = Field(None, description='', alias='59')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    GTBookingInst: Optional[int] = Field(None, description='', alias='427')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    ForexReq: Optional[bool] = Field(None, description='', alias='121')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    Price2: Optional[float] = Field(None, description='', alias='640')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    CoveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    MaxShow: Optional[float] = Field(None, description='', alias='210')
    TargetStrategy: Optional[int] = Field(None, description='', alias='847')
    TargetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    ParticipationRate: Optional[float] = Field(None, description='', alias='849')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    Designation: Optional[str] = Field(None, description='', alias='494')
    Parties: Optional[Parties] = None
    PreAllocGrp: Optional[PreAllocGrp] = None
    TrdgSesGrp: Optional[TrdgSesGrp] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    Stipulations: Optional[Stipulations] = None
    OrderQtyData: OrderQtyData = Field(..., description='OrderQtyData component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    YieldData: Optional[YieldData] = None
    CommissionData: Optional[CommissionData] = None
    PegInstructions: Optional[PegInstructions] = None
    DiscretionInstructions: Optional[DiscretionInstructions] = None

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
