"""FIX message model for MultilegOrderCancelReplace (AC).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.commissiondata import CommissionDataComponent
from ..components.discretioninstructions import DiscretionInstructionsComponent
from ..components.instrument import InstrumentComponent
from ..components.legordgrp import LegOrdGrpComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.parties import PartiesComponent
from ..components.peginstructions import PegInstructionsComponent
from ..components.preallocmleggrp import PreAllocMlegGrpComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class MultilegOrderCancelReplaceMessage(FIXMessageBase):
    """FIX message model for MultilegOrderCancelReplace."""

    MsgType: str = Field("AC", alias="35")

    OrderID: Optional[str] = Field(None, alias='37', description='')
    OrigClOrdID: str = Field(..., alias='41', description='')
    ClOrdID: str = Field(..., alias='11', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    ClOrdLinkID: Optional[str] = Field(None, alias='583', description='')
    OrigOrdModTime: Optional[datetime] = Field(None, alias='586', description='')
    TradeOriginationDate: Optional[date] = Field(None, alias='229', description='')
    TradeDate: Optional[date] = Field(None, alias='75', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    DayBookingInst: Optional[str] = Field(None, alias='589', description='')
    BookingUnit: Optional[str] = Field(None, alias='590', description='')
    PreallocMethod: Optional[str] = Field(None, alias='591', description='')
    AllocID: Optional[str] = Field(None, alias='70', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    CashMargin: Optional[str] = Field(None, alias='544', description='')
    ClearingFeeIndicator: Optional[str] = Field(None, alias='635', description='')
    HandlInst: Optional[str] = Field(None, alias='21', description='')
    ExecInst: Optional[List[str]] = Field(None, alias='18', description='')
    MinQty: Optional[float] = Field(None, alias='110', description='')
    MaxFloor: Optional[float] = Field(None, alias='111', description='')
    ExDestination: Optional[str] = Field(None, alias='100', description='')
    ProcessCode: Optional[str] = Field(None, alias='81', description='')
    Side: str = Field(..., alias='54', description='')
    PrevClosePx: Optional[float] = Field(None, alias='140', description='')
    LocateReqd: Optional[bool] = Field(None, alias='114', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    OrdType: str = Field(..., alias='40', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    StopPx: Optional[float] = Field(None, alias='99', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ComplianceID: Optional[str] = Field(None, alias='376', description='')
    SolicitedFlag: Optional[bool] = Field(None, alias='377', description='')
    IOIID: Optional[str] = Field(None, alias='23', description='')
    QuoteID: Optional[str] = Field(None, alias='117', description='')
    TimeInForce: Optional[str] = Field(None, alias='59', description='')
    EffectiveTime: Optional[datetime] = Field(None, alias='168', description='')
    ExpireDate: Optional[date] = Field(None, alias='432', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    GTBookingInst: Optional[int] = Field(None, alias='427', description='')
    OrderCapacity: Optional[str] = Field(None, alias='528', description='')
    OrderRestrictions: Optional[List[str]] = Field(None, alias='529', description='')
    CustOrderCapacity: Optional[int] = Field(None, alias='582', description='')
    ForexReq: Optional[bool] = Field(None, alias='121', description='')
    SettlCurrency: Optional[str] = Field(None, alias='120', description='')
    BookingType: Optional[int] = Field(None, alias='775', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    PositionEffect: Optional[str] = Field(None, alias='77', description='')
    CoveredOrUncovered: Optional[int] = Field(None, alias='203', description='')
    MaxShow: Optional[float] = Field(None, alias='210', description='')
    TargetStrategy: Optional[int] = Field(None, alias='847', description='')
    TargetStrategyParameters: Optional[str] = Field(None, alias='848', description='')
    ParticipationRate: Optional[float] = Field(None, alias='849', description='')
    CancellationRights: Optional[str] = Field(None, alias='480', description='')
    MoneyLaunderingStatus: Optional[str] = Field(None, alias='481', description='')
    RegistID: Optional[str] = Field(None, alias='513', description='')
    Designation: Optional[str] = Field(None, alias='494', description='')
    MultiLegRptTypeReq: Optional[int] = Field(None, alias='563', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    PreAllocMlegGrp: Optional[PreAllocMlegGrpComponent] = Field(None, description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')
    Instrument: InstrumentComponent = Field(..., description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    LegOrdGrp: LegOrdGrpComponent = Field(..., description='')
    OrderQtyData: OrderQtyDataComponent = Field(..., description='')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='')
    PegInstructions: Optional[PegInstructionsComponent] = Field(None, description='')
    DiscretionInstructions: Optional[DiscretionInstructionsComponent] = Field(None, description='')

