"""
FIX 4.4 TradeCaptureReport Message

This module contains the Pydantic model for the TradeCaptureReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.positionamountdata import PositionAmountData
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.trdcaprptsidegrp import TrdCapRptSideGrp
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class TradeCaptureReport(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["AE"] = Field("AE", alias='35')
    
    # Message-specific fields
    tradeReportID: Optional[str] = Field(None, description='', alias='571')
    tradeReportTransType: Optional[int] = Field(None, description='', alias='487')
    tradeReportType: Optional[int] = Field(None, description='', alias='856')
    tradeRequestID: Optional[str] = Field(None, description='', alias='568')
    trdType: Optional[int] = Field(None, description='', alias='828')
    trdSubType: Optional[int] = Field(None, description='', alias='829')
    secondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    transferReason: Optional[str] = Field(None, description='', alias='830')
    execType: Optional[str] = Field(None, description='', alias='150')
    totNumTradeReports: Optional[int] = Field(None, description='', alias='748')
    lastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    unsolicitedIndicator: Optional[bool] = Field(None, description='', alias='325')
    subscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    tradeReportRefID: Optional[str] = Field(None, description='', alias='572')
    secondaryTradeReportRefID: Optional[str] = Field(None, description='', alias='881')
    secondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    tradeLinkID: Optional[str] = Field(None, description='', alias='820')
    trdMatchID: Optional[str] = Field(None, description='', alias='880')
    execID: Optional[str] = Field(None, description='', alias='17')
    ordStatus: Optional[str] = Field(None, description='', alias='39')
    secondaryExecID: Optional[str] = Field(None, description='', alias='527')
    execRestatementReason: Optional[int] = Field(None, description='', alias='378')
    previouslyReported: Optional[bool] = Field(None, description='', alias='570')
    priceType: Optional[int] = Field(None, description='', alias='423')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    underlyingTradingSessionID: Optional[str] = Field(None, description='', alias='822')
    underlyingTradingSessionSubID: Optional[str] = Field(None, description='', alias='823')
    lastQty: Optional[float] = Field(None, description='', alias='32')
    lastPx: Optional[float] = Field(None, description='', alias='31')
    lastParPx: Optional[float] = Field(None, description='', alias='669')
    lastSpotRate: Optional[float] = Field(None, description='', alias='194')
    lastForwardPoints: Optional[float] = Field(None, description='', alias='195')
    lastMkt: Optional[str] = Field(None, description='', alias='30')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    clearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    avgPx: Optional[float] = Field(None, description='', alias='6')
    avgPxIndicator: Optional[int] = Field(None, description='', alias='819')
    multiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    tradeLegRefID: Optional[str] = Field(None, description='', alias='824')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    matchStatus: Optional[str] = Field(None, description='', alias='573')
    matchType: Optional[str] = Field(None, description='', alias='574')
    copyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    publishTrdIndicator: Optional[bool] = Field(None, description='', alias='852')
    shortSaleReason: Optional[int] = Field(None, description='', alias='853')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    positionAmountData: Optional[PositionAmountData] = Field(None, description='PositionAmountData component')
    trdInstrmtLegGrp: Optional[TrdInstrmtLegGrp] = Field(None, description='TrdInstrmtLegGrp component')
    trdRegTimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    trdCapRptSideGrp: Optional[TrdCapRptSideGrp] = Field(None, description='TrdCapRptSideGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
