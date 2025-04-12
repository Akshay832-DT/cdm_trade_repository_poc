"""
FIX 4.4 CollateralInquiry Message

This module contains the Pydantic model for the CollateralInquiry message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.collinqqualgrp import CollInqQualGrp
from src.models.fix.generated.components.execcollgrp import ExecCollGrp
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.trdcollgrp import TrdCollGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class CollateralInquiry(FIXMessageBase):
    """
    FIX 4.4 CollateralInquiry Message
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
    msgType: Literal["BB"] = Field("BB", alias='35')
    
    # Message-specific fields
    collInquiryID: Optional[str] = Field(None, description='', alias='909')
    subscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    responseTransportType: Optional[int] = Field(None, description='', alias='725')
    responseDestination: Optional[str] = Field(None, description='', alias='726')
    account: Optional[str] = Field(None, description='', alias='1')
    accountType: Optional[int] = Field(None, description='', alias='581')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    orderID: Optional[str] = Field(None, description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    quantity: Optional[float] = Field(None, description='', alias='53')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    currency: Optional[str] = Field(None, description='', alias='15')
    marginExcess: Optional[float] = Field(None, description='', alias='899')
    totalNetValue: Optional[float] = Field(None, description='', alias='900')
    cashOutstanding: Optional[float] = Field(None, description='', alias='901')
    side: Optional[str] = Field(None, description='', alias='54')
    price: Optional[float] = Field(None, description='', alias='44')
    priceType: Optional[int] = Field(None, description='', alias='423')
    accruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    endAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    startCash: Optional[float] = Field(None, description='', alias='921')
    endCash: Optional[float] = Field(None, description='', alias='922')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    settlSessID: Optional[str] = Field(None, description='', alias='716')
    settlSessSubID: Optional[str] = Field(None, description='', alias='717')
    clearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    collInqQualGrp: Optional[CollInqQualGrp] = Field(None, description='CollInqQualGrp component')
    parties: Optional[Parties] = Field(None, description='Parties component')
    execCollGrp: Optional[ExecCollGrp] = Field(None, description='ExecCollGrp component')
    trdCollGrp: Optional[TrdCollGrp] = Field(None, description='TrdCollGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    trdRegTimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    settlInstructionsData: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')

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
