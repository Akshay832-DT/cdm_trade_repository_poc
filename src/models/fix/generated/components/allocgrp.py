"""
FIX 4.4 AllocGrp Component

This module contains the Pydantic model for the AllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class AllocGrp(FIXMessageBase):
    """
    FIX 4.4 AllocGrp Component
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
    allocAccount: Optional[str] = Field(None, description='', alias='79')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    matchStatus: Optional[str] = Field(None, description='', alias='573')
    allocPrice: Optional[float] = Field(None, description='', alias='366')
    allocQty: Optional[float] = Field(None, description='', alias='80')
    individualAllocID: Optional[str] = Field(None, description='', alias='467')
    processCode: Optional[str] = Field(None, description='', alias='81')
    notifyBrokerOfCredit: Optional[bool] = Field(None, description='', alias='208')
    allocHandlInst: Optional[int] = Field(None, description='', alias='209')
    allocText: Optional[str] = Field(None, description='', alias='161')
    encodedAllocTextLen: Optional[int] = Field(None, description='', alias='360')
    encodedAllocText: Optional[str] = Field(None, description='', alias='361')
    allocAvgPx: Optional[float] = Field(None, description='', alias='153')
    allocNetMoney: Optional[float] = Field(None, description='', alias='154')
    settlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    allocSettlCurrAmt: Optional[float] = Field(None, description='', alias='737')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    allocSettlCurrency: Optional[str] = Field(None, description='', alias='736')
    settlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    settlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    allocAccruedInterestAmt: Optional[float] = Field(None, description='', alias='742')
    allocInterestAtMaturity: Optional[float] = Field(None, description='', alias='741')
    allocSettlInstType: Optional[int] = Field(None, description='', alias='780')
    nestedParties: Optional[str] = Field(None)
    commissionData: Optional[str] = Field(None)
    miscFeesGrp: Optional[str] = Field(None)
    clrInstGrp: Optional[str] = Field(None)
    settlInstructionsData: Optional[str] = Field(None)


class NoAllocs(FIXMessageBase):
    """
    NoAllocs group fields
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
    allocAccount: Optional[int] = Field(None, description='', alias='78')
    allocAcctIDSource: Optional[int] = Field(None, description='', alias='78')
    matchStatus: Optional[int] = Field(None, description='', alias='78')
    allocPrice: Optional[int] = Field(None, description='', alias='78')
    allocQty: Optional[int] = Field(None, description='', alias='78')
    individualAllocID: Optional[int] = Field(None, description='', alias='78')
    processCode: Optional[int] = Field(None, description='', alias='78')
    notifyBrokerOfCredit: Optional[int] = Field(None, description='', alias='78')
    allocHandlInst: Optional[int] = Field(None, description='', alias='78')
    allocText: Optional[int] = Field(None, description='', alias='78')
    encodedAllocTextLen: Optional[int] = Field(None, description='', alias='78')
    encodedAllocText: Optional[int] = Field(None, description='', alias='78')
    allocAvgPx: Optional[int] = Field(None, description='', alias='78')
    allocNetMoney: Optional[int] = Field(None, description='', alias='78')
    settlCurrAmt: Optional[int] = Field(None, description='', alias='78')
    allocSettlCurrAmt: Optional[int] = Field(None, description='', alias='78')
    settlCurrency: Optional[int] = Field(None, description='', alias='78')
    allocSettlCurrency: Optional[int] = Field(None, description='', alias='78')
    settlCurrFxRate: Optional[int] = Field(None, description='', alias='78')
    settlCurrFxRateCalc: Optional[int] = Field(None, description='', alias='78')
    allocAccruedInterestAmt: Optional[int] = Field(None, description='', alias='78')
    allocInterestAtMaturity: Optional[int] = Field(None, description='', alias='78')
    allocSettlInstType: Optional[int] = Field(None, description='', alias='78')

    noAllocss: List[NoAllocs] = Field(default_factory=list)
