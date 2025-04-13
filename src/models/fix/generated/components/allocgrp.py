"""
FIX 4.4 AllocGrp Component

This module contains the Pydantic model for the AllocGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoAllocsGroup(FIXComponentBase):
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
    
    AllocAccount: Optional[str] = Field(None, description='', alias='79')
    AllocAcctIDSource: Optional[int] = Field(None, description='', alias='661')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    AllocPrice: Optional[float] = Field(None, description='', alias='366')
    AllocQty: Optional[float] = Field(None, description='', alias='80')
    IndividualAllocID: Optional[str] = Field(None, description='', alias='467')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    NotifyBrokerOfCredit: Optional[bool] = Field(None, description='', alias='208')
    AllocHandlInst: Optional[int] = Field(None, description='', alias='209')
    AllocText: Optional[str] = Field(None, description='', alias='161')
    EncodedAllocTextLen: Optional[int] = Field(None, description='', alias='360')
    EncodedAllocText: Optional[str] = Field(None, description='', alias='361')
    AllocAvgPx: Optional[float] = Field(None, description='', alias='153')
    AllocNetMoney: Optional[float] = Field(None, description='', alias='154')
    SettlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    AllocSettlCurrAmt: Optional[float] = Field(None, description='', alias='737')
    SettlCurrency: Optional[str] = Field(None, description='', alias='120')
    AllocSettlCurrency: Optional[str] = Field(None, description='', alias='736')
    SettlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    SettlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    AllocAccruedInterestAmt: Optional[float] = Field(None, description='', alias='742')
    AllocInterestAtMaturity: Optional[float] = Field(None, description='', alias='741')
    AllocSettlInstType: Optional[int] = Field(None, description='', alias='780')


class AllocGrpComponent(FIXComponentBase):
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
    
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='NestedParties component')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='CommissionData component')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='MiscFeesGrp component')
    ClrInstGrp: Optional[ClrInstGrpComponent] = Field(None, description='ClrInstGrp component')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='SettlInstructionsData component')
    NoAllocs: Optional[int] = Field(None, description='Number of NoAllocs entries', alias='')
    NoAllocs_items: List[NoAllocsGroup] = Field(default_factory=list)
