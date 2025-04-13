"""
FIX 4.4 AllocGrp Component

This module contains the Pydantic model for the AllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.nestedparties import NestedParties
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrp
from src.models.fix.generated.components.clrinstgrp import ClrInstGrp
from src.models.fix.generated.components.settlinstructionsdata import SettlInstructionsData


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
    
    nestedParties: Optional[NestedParties] = Field(None, description='NestedParties component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
    miscFeesGrp: Optional[MiscFeesGrp] = Field(None, description='MiscFeesGrp component')
    clrInstGrp: Optional[ClrInstGrp] = Field(None, description='ClrInstGrp component')
    settlInstructionsData: Optional[SettlInstructionsData] = Field(None, description='SettlInstructionsData component')
    noAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='78')
    noAllocs_items: List[NoAllocs] = Field(default_factory=list)
