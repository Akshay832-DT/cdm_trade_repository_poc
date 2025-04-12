"""
FIX 4.4 TradeCaptureReport Message

This module contains the Pydantic model for the TradeCaptureReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.financingdetails import FinancingDetails
from ..components.instrument import Instrument
from ..components.orderqtydata import OrderQtyData
from ..components.positionamountdata import PositionAmountData
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.trdcaprptsidegrp import TrdCapRptSideGrp
from ..components.trdinstrmtleggrp import TrdInstrmtLegGrp
from ..components.trdregtimestamps import TrdRegTimestamps
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class TradeCaptureReport(TradeModel):
    """
    FIX 4.4 TradeCaptureReport Message
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
    MsgType: Literal["AE"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    TradeReportID: str = Field(None, description='', alias='571')
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
    PreviouslyReported: bool = Field(None, description='', alias='570')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    UnderlyingTradingSessionID: Optional[str] = Field(None, description='', alias='822')
    UnderlyingTradingSessionSubID: Optional[str] = Field(None, description='', alias='823')
    LastQty: float = Field(None, description='', alias='32')
    LastPx: float = Field(None, description='', alias='31')
    LastParPx: Optional[float] = Field(None, description='', alias='669')
    LastSpotRate: Optional[float] = Field(None, description='', alias='194')
    LastForwardPoints: Optional[float] = Field(None, description='', alias='195')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    TradeDate: date = Field(None, description='', alias='75')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    AvgPx: Optional[float] = Field(None, description='', alias='6')
    AvgPxIndicator: Optional[int] = Field(None, description='', alias='819')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    TradeLegRefID: Optional[str] = Field(None, description='', alias='824')
    TransactTime: datetime = Field(None, description='', alias='60')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    MatchType: Optional[str] = Field(None, description='', alias='574')
    CopyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    PublishTrdIndicator: Optional[bool] = Field(None, description='', alias='852')
    ShortSaleReason: Optional[int] = Field(None, description='', alias='853')
    Instrument: Instrument = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetails] = None
    OrderQtyData: Optional[OrderQtyData] = None
    YieldData: Optional[YieldData] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    PositionAmountData: Optional[PositionAmountData] = None
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrp] = None
    TrdRegTimestamps: Optional[TrdRegTimestamps] = None
    TrdCapRptSideGrp: TrdCapRptSideGrp = Field(..., description='TrdCapRptSideGrp component')

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
