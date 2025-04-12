"""
FIX 4.4 Confirmation Message

This module contains the Pydantic model for the Confirmation message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.commissiondata import CommissionData
from ..components.cpctyconfgrp import CpctyConfGrp
from ..components.financingdetails import FinancingDetails
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.instrumentextension import InstrumentExtension
from ..components.miscfeesgrp import MiscFeesGrp
from ..components.ordallocgrp import OrdAllocGrp
from ..components.parties import Parties
from ..components.settlinstructionsdata import SettlInstructionsData
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.trdregtimestamps import TrdRegTimestamps
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class Confirmation(TradeModel):
    """
    FIX 4.4 Confirmation Message
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
    MsgType: Literal["AK"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    ConfirmID: str = Field(None, description='', alias='664')
    ConfirmRefID: Optional[str] = Field(None, description='', alias='772')
    ConfirmReqID: Optional[str] = Field(None, description='', alias='859')
    ConfirmTransType: int = Field(None, description='', alias='666')
    ConfirmType: int = Field(None, description='', alias='773')
    CopyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    LegalConfirm: Optional[bool] = Field(None, description='', alias='650')
    ConfirmStatus: int = Field(None, description='', alias='665')
    AllocID: Optional[str] = Field(None, description='', alias='70')
    SecondaryAllocID: Optional[str] = Field(None, description='', alias='793')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    TransactTime: datetime = Field(None, description='', alias='60')
    TradeDate: date = Field(None, description='', alias='75')
    AllocQty: float = Field(None, description='', alias='80')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Side: str = Field(None, description='', alias='54')
    Currency: Optional[str] = Field(None, description='', alias='15')
    LastMkt: Optional[str] = Field(None, description='', alias='30')
    AllocAccount: str = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    AllocAccountType: Optional[int] = Field(None, description='', alias='798')
    AvgPx: float = Field(None, description='', alias='6')
    AvgPxPrecision: Optional[int] = Field(None, description='', alias='74')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    AvgParPx: Optional[float] = Field(None, description='', alias='860')
    ReportedPx: Optional[float] = Field(None, description='', alias='861')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    GrossTradeAmt: float = Field(None, description='', alias='381')
    NumDaysInterest: Optional[int] = Field(None, description='', alias='157')
    ExDate: Optional[date] = Field(None, description='', alias='230')
    AccruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    AccruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    InterestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    EndAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    StartCash: Optional[float] = Field(None, description='', alias='921')
    EndCash: Optional[float] = Field(None, description='', alias='922')
    Concession: Optional[float] = Field(None, description='', alias='238')
    TotalTakedown: Optional[float] = Field(None, description='', alias='237')
    NetMoney: float = Field(None, description='', alias='118')
    MaturityNetMoney: Optional[float] = Field(None, description='', alias='890')
    SettlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    SettlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    SharedCommission: Optional[float] = Field(None, description='', alias='858')
    Parties: Optional[Parties] = None
    OrdAllocGrp: Optional[OrdAllocGrp] = None
    TrdRegTimestamps: Optional[TrdRegTimestamps] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    InstrumentExtension: Optional[InstrumentExtension] = None
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: UndInstrmtGrp = Field(..., description='UndInstrmtGrp component')
    InstrmtLegGrp: InstrmtLegGrp = Field(..., description='InstrmtLegGrp component')
    YieldData: Optional[YieldData] = None
    CpctyConfGrp: CpctyConfGrp = Field(..., description='CpctyConfGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    SettlInstructionsData: Optional[SettlInstructionsData] = None
    CommissionData: Optional[CommissionData] = None
    Stipulations: Optional[Stipulations] = None
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
