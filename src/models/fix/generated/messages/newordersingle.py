from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.preallocgrp import PreAllocGrpComponent
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent
from src.models.fix.generated.components.commissiondata import CommissionDataComponent
from src.models.fix.generated.components.peginstructions import PegInstructionsComponent
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructionsComponent

class NewOrderSingle(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ClOrdID: str = Field(..., description='', alias='11')
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
    Side: str = Field(..., description='', alias='54')
    LocateReqd: Optional[bool] = Field(None, description='', alias='114')
    TransactTime: datetime = Field(..., description='', alias='60')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    OrdType: str = Field(..., description='', alias='40')
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
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    PreAllocGrp: Optional[PreAllocGrpComponent] = Field(None, description='PreAllocGrp component')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='TrdgSesGrp component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    OrderQtyData: OrderQtyDataComponent = Field(..., description='OrderQtyData component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='CommissionData component')
    PegInstructions: Optional[PegInstructionsComponent] = Field(None, description='PegInstructions component')
    DiscretionInstructions: Optional[DiscretionInstructionsComponent] = Field(None, description='DiscretionInstructions component')

