"""FIX message model for TradeCaptureReport (AE).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrument import InstrumentComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.positionamountdata import PositionAmountDataComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.trdcaprptsidegrp import TrdCapRptSideGrpComponent
from ..components.trdinstrmtleggrp import TrdInstrmtLegGrpComponent
from ..components.trdregtimestamps import TrdRegTimestampsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class TradeCaptureReportMessage(FIXMessageBase):
    """FIX message model for TradeCaptureReport."""

    MsgType: str = Field("AE", alias="35")

    TradeReportID: str = Field(..., alias='571', description='')
    TradeReportTransType: Optional[int] = Field(None, alias='487', description='')
    TradeReportType: Optional[int] = Field(None, alias='856', description='')
    TradeRequestID: Optional[str] = Field(None, alias='568', description='')
    TrdType: Optional[int] = Field(None, alias='828', description='')
    TrdSubType: Optional[int] = Field(None, alias='829', description='')
    SecondaryTrdType: Optional[int] = Field(None, alias='855', description='')
    TransferReason: Optional[str] = Field(None, alias='830', description='')
    ExecType: Optional[str] = Field(None, alias='150', description='')
    TotNumTradeReports: Optional[int] = Field(None, alias='748', description='')
    LastRptRequested: Optional[bool] = Field(None, alias='912', description='')
    UnsolicitedIndicator: Optional[bool] = Field(None, alias='325', description='')
    SubscriptionRequestType: Optional[str] = Field(None, alias='263', description='')
    TradeReportRefID: Optional[str] = Field(None, alias='572', description='')
    SecondaryTradeReportRefID: Optional[str] = Field(None, alias='881', description='')
    SecondaryTradeReportID: Optional[str] = Field(None, alias='818', description='')
    TradeLinkID: Optional[str] = Field(None, alias='820', description='')
    TrdMatchID: Optional[str] = Field(None, alias='880', description='')
    ExecID: Optional[str] = Field(None, alias='17', description='')
    OrdStatus: Optional[str] = Field(None, alias='39', description='')
    SecondaryExecID: Optional[str] = Field(None, alias='527', description='')
    ExecRestatementReason: Optional[int] = Field(None, alias='378', description='')
    PreviouslyReported: bool = Field(..., alias='570', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    UnderlyingTradingSessionID: Optional[str] = Field(None, alias='822', description='')
    UnderlyingTradingSessionSubID: Optional[str] = Field(None, alias='823', description='')
    LastQty: float = Field(..., alias='32', description='')
    LastPx: float = Field(..., alias='31', description='')
    LastParPx: Optional[float] = Field(None, alias='669', description='')
    LastSpotRate: Optional[float] = Field(None, alias='194', description='')
    LastForwardPoints: Optional[float] = Field(None, alias='195', description='')
    LastMkt: Optional[str] = Field(None, alias='30', description='')
    TradeDate: date = Field(..., alias='75', description='')
    ClearingBusinessDate: Optional[date] = Field(None, alias='715', description='')
    AvgPx: Optional[float] = Field(None, alias='6', description='')
    AvgPxIndicator: Optional[int] = Field(None, alias='819', description='')
    MultiLegReportingType: Optional[str] = Field(None, alias='442', description='')
    TradeLegRefID: Optional[str] = Field(None, alias='824', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    SettlType: Optional[str] = Field(None, alias='63', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    MatchType: Optional[str] = Field(None, alias='574', description='')
    CopyMsgIndicator: Optional[bool] = Field(None, alias='797', description='')
    PublishTrdIndicator: Optional[bool] = Field(None, alias='852', description='')
    ShortSaleReason: Optional[int] = Field(None, alias='853', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    PositionAmountData: Optional[PositionAmountDataComponent] = Field(None, description='')
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrpComponent] = Field(None, description='')
    TrdRegTimestamps: Optional[TrdRegTimestampsComponent] = Field(None, description='')
    TrdCapRptSideGrp: TrdCapRptSideGrpComponent = Field(..., description='')

