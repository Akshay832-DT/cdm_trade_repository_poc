"""
FIX 4.4 ExecutionReport Message

This module contains the Pydantic model for the ExecutionReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.commissiondata import CommissionData
from ..components.contamtgrp import ContAmtGrp
from ..components.contragrp import ContraGrp
from ..components.discretioninstructions import DiscretionInstructions
from ..components.financingdetails import FinancingDetails
from ..components.instrmtlegexecgrp import InstrmtLegExecGrp
from ..components.instrument import Instrument
from ..components.miscfeesgrp import MiscFeesGrp
from ..components.orderqtydata import OrderQtyData
from ..components.parties import Parties
from ..components.peginstructions import PegInstructions
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class ExecutionReport(TradeModel):
    """
    FIX 4.4 ExecutionReport Message
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
    MsgType: Literal["8"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    OrderID: str = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    SecondaryExecID: Optional[str] = Field(None, description='', alias='527')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrigClOrdID: Optional[str] = Field(None, description='', alias='41')
    ClOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    QuoteRespID: Optional[str] = Field(None, description='', alias='693')
    OrdStatusReqID: Optional[str] = Field(None, description='', alias='790')
    MassStatusReqID: Optional[str] = Field(None, description='', alias='584')
    TotNumReports: Optional[int] = Field(None, description='', alias='911')
    LastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    TradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    ListID: Optional[str] = Field(None, description='', alias='66')
    CrossID: Optional[str] = Field(None, description='', alias='548')
    OrigCrossID: Optional[str] = Field(None, description='', alias='551')
    CrossType: Optional[int] = Field(None, description='', alias='549')
    ExecID: str = Field(None, description='', alias='17')
    ExecRefID: Optional[str] = Field(None, description='', alias='19')
    ExecType: str = Field(None, description='', alias='150')
    OrdStatus: str = Field(None, description='', alias='39')
    WorkingIndicator: Optional[bool] = Field(None, description='', alias='636')
    OrdRejReason: Optional[int] = Field(None, description='', alias='103')
    ExecRestatementReason: Optional[int] = Field(None, description='', alias='378')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    DayBookingInst: Optional[str] = Field(None, description='', alias='589')
    BookingUnit: Optional[str] = Field(None, description='', alias='590')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    CashMargin: Optional[str] = Field(None, description='', alias='544')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    Side: str = Field(None, description='', alias='54')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    OrdType: Optional[str] = Field(None, description='', alias='40')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    StopPx: Optional[float] = Field(None, description='', alias='99')
    PeggedPrice: Optional[float] = Field(None, description='', alias='839')
    DiscretionPrice: Optional[float] = Field(None, description='', alias='845')
    TargetStrategy: Optional[int] = Field(None, description='', alias='847')
    TargetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    ParticipationRate: Optional[float] = Field(None, description='', alias='849')
    TargetStrategyPerformance: Optional[float] = Field(None, description='', alias='850')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    SolicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    TimeInForce: Optional[str] = Field(None, description='', alias='59')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    LastQty: Optional[float] = Field(None, description='', alias='32')
    UnderlyingLastQty: Optional[float] = Field(None, description='', alias='652')
    LastPx: Optional[float] = Field(None, description='', alias='31')
    UnderlyingLastPx: Optional[float] = Field(None, description='', alias='651')
    LastParPx: Optional[float] = Field(None, description='', alias='669')
    LastSpotRate: Optional[float] = Field(None, description='', alias='194')
    LastForwardPoints: Optional[float] = Field(None, description='', alias='195')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TimeBracket: Optional[str] = Field(None, description='', alias='943')
    LastCapacity: Optional[str] = Field(None, description='', alias='29')
    LeavesQty: float = Field(None, description='', alias='151')
    CumQty: float = Field(None, description='', alias='14')
    AvgPx: float = Field(None, description='', alias='6')
    DayOrderQty: Optional[float] = Field(None, description='', alias='424')
    DayCumQty: Optional[float] = Field(None, description='', alias='425')
    DayAvgPx: Optional[float] = Field(None, description='', alias='426')
    GTBookingInst: Optional[int] = Field(None, description='', alias='427')
    TradeDate: Optional[date] = Field(None, description='', alias='75')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    ReportToExch: Optional[bool] = Field(None, description='', alias='113')
    GrossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    NumDaysInterest: Optional[int] = Field(None, description='', alias='157')
    ExDate: Optional[date] = Field(None, description='', alias='230')
    AccruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    InterestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    TradedFlatSwitch: Optional[bool] = Field(None, description='', alias='258')
    BasisFeatureDate: Optional[date] = Field(None, description='', alias='259')
    BasisFeaturePrice: Optional[float] = Field(None, description='', alias='260')
    Concession: Optional[float] = Field(None, description='', alias='238')
    TotalTakedown: Optional[float] = Field(None, description='', alias='237')
    NetMoney: Optional[float] = Field(None, description='', alias='118')
    SettlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    SettlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    HandlInst: Optional[str] = Field(None, description='', alias='21')
    MinQty: Optional[float] = Field(None, description='', alias='110')
    MaxFloor: Optional[float] = Field(None, description='', alias='111')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    MaxShow: Optional[float] = Field(None, description='', alias='210')
    BookingType: Optional[int] = Field(None, description='', alias='775')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    SettlDate2: Optional[date] = Field(None, description='', alias='193')
    OrderQty2: Optional[float] = Field(None, description='', alias='192')
    LastForwardPoints2: Optional[float] = Field(None, description='', alias='641')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    Designation: Optional[str] = Field(None, description='', alias='494')
    TransBkdTime: Optional[datetime] = Field(None, description='', alias='483')
    ExecValuationPoint: Optional[datetime] = Field(None, description='', alias='515')
    ExecPriceType: Optional[str] = Field(None, description='', alias='484')
    ExecPriceAdjustment: Optional[float] = Field(None, description='', alias='485')
    PriorityIndicator: Optional[int] = Field(None, description='', alias='638')
    PriceImprovement: Optional[float] = Field(None, description='', alias='639')
    LastLiquidityInd: Optional[int] = Field(None, description='', alias='851')
    CopyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    Parties: Optional[Parties] = None
    ContraGrp: Optional[ContraGrp] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    Stipulations: Optional[Stipulations] = None
    OrderQtyData: Optional[OrderQtyData] = None
    PegInstructions: Optional[PegInstructions] = None
    DiscretionInstructions: Optional[DiscretionInstructions] = None
    CommissionData: Optional[CommissionData] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    YieldData: Optional[YieldData] = None
    ContAmtGrp: Optional[ContAmtGrp] = None
    InstrmtLegExecGrp: Optional[InstrmtLegExecGrp] = None
    MiscFeesGrp: Optional[MiscFeesGrp] = None

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
