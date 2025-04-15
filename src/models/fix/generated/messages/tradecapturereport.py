"""
FIX TradeCaptureReport Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
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


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
PositionAmountDataComponent = ForwardRef('PositionAmountDataComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
TrdCapRptSideGrpComponent = ForwardRef('TrdCapRptSideGrpComponent')
TrdInstrmtLegGrpComponent = ForwardRef('TrdInstrmtLegGrpComponent')
TrdRegTimestampsComponent = ForwardRef('TrdRegTimestampsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class TradeCaptureReportMessage(FIXMessageBase):
    """TradeCaptureReport Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["TradeCaptureReport"] = Field("TradeCaptureReport", alias="35", description="Message Type")

    TradeReportID: Optional[str] = Field(None, alias="571", description="")
    TradeReportTransType: Optional[int] = Field(None, alias="487", description="")
    TradeReportType: Optional[int] = Field(None, alias="856", description="")
    TradeRequestID: Optional[str] = Field(None, alias="568", description="")
    TrdType: Optional[int] = Field(None, alias="828", description="")
    TrdSubType: Optional[int] = Field(None, alias="829", description="")
    SecondaryTrdType: Optional[int] = Field(None, alias="855", description="")
    TransferReason: Optional[str] = Field(None, alias="830", description="")
    ExecType: Optional[str] = Field(None, alias="150", description="")
    TotNumTradeReports: Optional[int] = Field(None, alias="748", description="")
    LastRptRequested: Optional[bool] = Field(None, alias="912", description="")
    UnsolicitedIndicator: Optional[bool] = Field(None, alias="325", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    TradeReportRefID: Optional[str] = Field(None, alias="572", description="")
    SecondaryTradeReportRefID: Optional[str] = Field(None, alias="881", description="")
    SecondaryTradeReportID: Optional[str] = Field(None, alias="818", description="")
    TradeLinkID: Optional[str] = Field(None, alias="820", description="")
    TrdMatchID: Optional[str] = Field(None, alias="880", description="")
    ExecID: Optional[str] = Field(None, alias="17", description="")
    OrdStatus: Optional[str] = Field(None, alias="39", description="")
    SecondaryExecID: Optional[str] = Field(None, alias="527", description="")
    ExecRestatementReason: Optional[int] = Field(None, alias="378", description="")
    PreviouslyReported: Optional[bool] = Field(None, alias="570", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    UnderlyingTradingSessionID: Optional[str] = Field(None, alias="822", description="")
    UnderlyingTradingSessionSubID: Optional[str] = Field(None, alias="823", description="")
    LastQty: Optional[float] = Field(None, alias="32", description="")
    LastPx: Optional[float] = Field(None, alias="31", description="")
    LastParPx: Optional[float] = Field(None, alias="669", description="")
    LastSpotRate: Optional[float] = Field(None, alias="194", description="")
    LastForwardPoints: Optional[float] = Field(None, alias="195", description="")
    LastMkt: Optional[str] = Field(None, alias="30", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    AvgPx: Optional[float] = Field(None, alias="6", description="")
    AvgPxIndicator: Optional[int] = Field(None, alias="819", description="")
    MultiLegReportingType: Optional[str] = Field(None, alias="442", description="")
    TradeLegRefID: Optional[str] = Field(None, alias="824", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    MatchStatus: Optional[str] = Field(None, alias="573", description="")
    MatchType: Optional[str] = Field(None, alias="574", description="")
    CopyMsgIndicator: Optional[bool] = Field(None, alias="797", description="")
    PublishTrdIndicator: Optional[bool] = Field(None, alias="852", description="")
    ShortSaleReason: Optional[int] = Field(None, alias="853", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    PositionAmountData: ForwardRef('PositionAmountDataComponent') = Field(None, description="PositionAmountData Component")
    TrdInstrmtLegGrp: ForwardRef('TrdInstrmtLegGrpComponent') = Field(None, description="TrdInstrmtLegGrp Component")
    TrdRegTimestamps: ForwardRef('TrdRegTimestampsComponent') = Field(None, description="TrdRegTimestamps Component")
    TrdCapRptSideGrp: ForwardRef('TrdCapRptSideGrpComponent') = Field(None, description="TrdCapRptSideGrp Component")

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
        if self.TradeReportID is not None:
            fields.append(f"TradeReportID={self.TradeReportID}")
        if self.TradeReportTransType is not None:
            fields.append(f"TradeReportTransType={self.TradeReportTransType}")
        if self.TradeReportType is not None:
            fields.append(f"TradeReportType={self.TradeReportType}")
        if self.TradeRequestID is not None:
            fields.append(f"TradeRequestID={self.TradeRequestID}")
        if self.TrdType is not None:
            fields.append(f"TrdType={self.TrdType}")
        if self.TrdSubType is not None:
            fields.append(f"TrdSubType={self.TrdSubType}")
        if self.SecondaryTrdType is not None:
            fields.append(f"SecondaryTrdType={self.SecondaryTrdType}")
        if self.TransferReason is not None:
            fields.append(f"TransferReason={self.TransferReason}")
        if self.ExecType is not None:
            fields.append(f"ExecType={self.ExecType}")
        if self.TotNumTradeReports is not None:
            fields.append(f"TotNumTradeReports={self.TotNumTradeReports}")
        if self.LastRptRequested is not None:
            fields.append(f"LastRptRequested={self.LastRptRequested}")
        if self.UnsolicitedIndicator is not None:
            fields.append(f"UnsolicitedIndicator={self.UnsolicitedIndicator}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.TradeReportRefID is not None:
            fields.append(f"TradeReportRefID={self.TradeReportRefID}")
        if self.SecondaryTradeReportRefID is not None:
            fields.append(f"SecondaryTradeReportRefID={self.SecondaryTradeReportRefID}")
        if self.SecondaryTradeReportID is not None:
            fields.append(f"SecondaryTradeReportID={self.SecondaryTradeReportID}")
        if self.TradeLinkID is not None:
            fields.append(f"TradeLinkID={self.TradeLinkID}")
        if self.TrdMatchID is not None:
            fields.append(f"TrdMatchID={self.TrdMatchID}")
        if self.ExecID is not None:
            fields.append(f"ExecID={self.ExecID}")
        if self.OrdStatus is not None:
            fields.append(f"OrdStatus={self.OrdStatus}")
        if self.SecondaryExecID is not None:
            fields.append(f"SecondaryExecID={self.SecondaryExecID}")
        if self.ExecRestatementReason is not None:
            fields.append(f"ExecRestatementReason={self.ExecRestatementReason}")
        if self.PreviouslyReported is not None:
            fields.append(f"PreviouslyReported={self.PreviouslyReported}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.UnderlyingTradingSessionID is not None:
            fields.append(f"UnderlyingTradingSessionID={self.UnderlyingTradingSessionID}")
        if self.UnderlyingTradingSessionSubID is not None:
            fields.append(f"UnderlyingTradingSessionSubID={self.UnderlyingTradingSessionSubID}")
        if self.LastQty is not None:
            fields.append(f"LastQty={self.LastQty}")
        if self.LastPx is not None:
            fields.append(f"LastPx={self.LastPx}")
        if self.LastParPx is not None:
            fields.append(f"LastParPx={self.LastParPx}")
        if self.LastSpotRate is not None:
            fields.append(f"LastSpotRate={self.LastSpotRate}")
        if self.LastForwardPoints is not None:
            fields.append(f"LastForwardPoints={self.LastForwardPoints}")
        if self.LastMkt is not None:
            fields.append(f"LastMkt={self.LastMkt}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.ClearingBusinessDate is not None:
            fields.append(f"ClearingBusinessDate={self.ClearingBusinessDate}")
        if self.AvgPx is not None:
            fields.append(f"AvgPx={self.AvgPx}")
        if self.AvgPxIndicator is not None:
            fields.append(f"AvgPxIndicator={self.AvgPxIndicator}")
        if self.MultiLegReportingType is not None:
            fields.append(f"MultiLegReportingType={self.MultiLegReportingType}")
        if self.TradeLegRefID is not None:
            fields.append(f"TradeLegRefID={self.TradeLegRefID}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.MatchStatus is not None:
            fields.append(f"MatchStatus={self.MatchStatus}")
        if self.MatchType is not None:
            fields.append(f"MatchType={self.MatchType}")
        if self.CopyMsgIndicator is not None:
            fields.append(f"CopyMsgIndicator={self.CopyMsgIndicator}")
        if self.PublishTrdIndicator is not None:
            fields.append(f"PublishTrdIndicator={self.PublishTrdIndicator}")
        if self.ShortSaleReason is not None:
            fields.append(f"ShortSaleReason={self.ShortSaleReason}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.OrderQtyData is not None:
            fields.append(f"OrderQtyData={self.OrderQtyData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.PositionAmountData is not None:
            fields.append(f"PositionAmountData={self.PositionAmountData}")
        if self.TrdInstrmtLegGrp is not None:
            fields.append(f"TrdInstrmtLegGrp={self.TrdInstrmtLegGrp}")
        if self.TrdRegTimestamps is not None:
            fields.append(f"TrdRegTimestamps={self.TrdRegTimestamps}")
        if self.TrdCapRptSideGrp is not None:
            fields.append(f"TrdCapRptSideGrp={self.TrdCapRptSideGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
TradeCaptureReportMessage.model_rebuild()
