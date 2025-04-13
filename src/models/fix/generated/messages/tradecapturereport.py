from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.positionamountdata import PositionAmountDataComponent
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrpComponent
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestampsComponent
from src.models.fix.generated.components.trdcaprptsidegrp import TrdCapRptSideGrpComponent

class TradeCaptureReport(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    TradeReportID: str = Field(..., description='', alias='571')
    TradeReportTransType: Optional[int] = Field(None, description='', alias='487')
    TradeReportType: Optional[int] = Field(None, description='', alias='856')
    TradeRequestID: Optional[str] = Field(None, description='', alias='568')
    TrdType: Optional[int] = Field(None, description='', alias='828')
    TrdSubType: Optional[int] = Field(None, description='', alias='829')
    SecondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    TransferReason: Optional[str] = Field(None, description='', alias='830')
    ExecType: Optional[str] = Field(None, description='', alias='150')
    TotNumTradeReports: Optional[int] = Field(None, description='', alias='748')
    LastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    UnsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TradeReportRefID: Optional[str] = Field(None, description='', alias='572')
    SecondaryTradeReportRefID: Optional[str] = Field(None, description='', alias='881')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    TradeLinkID: Optional[str] = Field(None, description='', alias='820')
    TrdMatchID: Optional[str] = Field(None, description='', alias='880')
    ExecID: Optional[str] = Field(None, description='', alias='17')
    OrdStatus: Optional[str] = Field(None, description='', alias='39')
    SecondaryExecID: Optional[str] = Field(None, description='', alias='527')
    ExecRestatementReason: Optional[int] = Field(None, description='', alias='378')
    PreviouslyReported: bool = Field(..., description='', alias='570')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    UnderlyingTradingSessionID: Optional[str] = Field(None, description='', alias='822')
    UnderlyingTradingSessionSubID: Optional[str] = Field(None, description='', alias='823')
    LastQty: float = Field(..., description='', alias='32')
    LastPx: float = Field(..., description='', alias='31')
    LastParPx: Optional[float] = Field(None, description='', alias='669')
    LastSpotRate: Optional[float] = Field(None, description='', alias='194')
    LastForwardPoints: Optional[float] = Field(None, description='', alias='195')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradeDate: date = Field(..., description='', alias='75')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    AvgPx: Optional[float] = Field(None, description='', alias='6')
    AvgPxIndicator: Optional[int] = Field(None, description='', alias='819')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    TradeLegRefID: Optional[str] = Field(None, description='', alias='824')
    TransactTime: datetime = Field(..., description='', alias='60')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    MatchType: Optional[str] = Field(None, description='', alias='574')
    CopyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    PublishTrdIndicator: Optional[bool] = Field(None, description='', alias='852')
    ShortSaleReason: Optional[int] = Field(None, description='', alias='853')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='OrderQtyData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    PositionAmountData: Optional[PositionAmountDataComponent] = Field(None, description='PositionAmountData component')
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrpComponent] = Field(None, description='TrdInstrmtLegGrp component')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='TrdRegTimestamps component')
    TrdCapRptSideGrp: TrdCapRptSideGrpComponent = Field(..., description='TrdCapRptSideGrp component')

