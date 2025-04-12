"""
FIX 4.4 CollateralReport Message

This module contains the Pydantic model for the CollateralReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.execcollgrp import ExecCollGrp
from ..components.financingdetails import FinancingDetails
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.miscfeesgrp import MiscFeesGrp
from ..components.parties import Parties
from ..components.settlinstructionsdata import SettlInstructionsData
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.trdcollgrp import TrdCollGrp
from ..components.trdregtimestamps import TrdRegTimestamps
from ..components.undinstrmtgrp import UndInstrmtGrp


class CollateralReport(TradeModel):
    """
    FIX 4.4 CollateralReport Message
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
    MsgType: Literal["BA"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    CollRptID: str = Field(None, description='', alias='908')
    CollInquiryID: Optional[str] = Field(None, description='', alias='909')
    CollStatus: int = Field(None, description='', alias='910')
    TotNumReports: Optional[int] = Field(None, description='', alias='911')
    LastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    Account: Optional[str] = Field(None, description='', alias='1')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    Quantity: Optional[float] = Field(None, description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Currency: Optional[str] = Field(None, description='', alias='15')
    MarginExcess: Optional[float] = Field(None, description='', alias='899')
    TotalNetValue: Optional[float] = Field(None, description='', alias='900')
    CashOutstanding: Optional[float] = Field(None, description='', alias='901')
    Side: Optional[str] = Field(None, description='', alias='54')
    Price: Optional[float] = Field(None, description='', alias='44')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[Parties] = None
    ExecCollGrp: Optional[ExecCollGrp] = None
    TrdCollGrp: Optional[TrdCollGrp] = None
    Instrument: Optional[Instrument] = None
    FinancingDetails: Optional[FinancingDetails] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    TrdRegTimestamps: Optional[TrdRegTimestamps] = None
    MiscFeesGrp: Optional[MiscFeesGrp] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    Stipulations: Optional[Stipulations] = None
    SettlInstructionsData: Optional[SettlInstructionsData] = None

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
