"""
FIX Component Model - AllocGrp
"""

from ..base import FIXComponentBase
from .clrinstgrp import ClrInstGrpComponent
from .commissiondata import CommissionDataComponent
from .miscfeesgrp import MiscFeesGrpComponent
from .nestedparties import NestedPartiesComponent
from .settlinstructionsdata import SettlInstructionsDataComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoAllocsGroup(FIXComponentBase):

    """FIX Group - NoAllocs"""

    AllocAccount: Optional[str] = Field(None, alias='79', description='')
    AllocAcctIDSource: Optional[int] = Field(None, alias='661', description='')
    MatchStatus: Optional[str] = Field(None, alias='573', description='')
    AllocPrice: Optional[float] = Field(None, alias='366', description='')
    AllocQty: Optional[float] = Field(None, alias='80', description='')
    IndividualAllocID: Optional[str] = Field(None, alias='467', description='')
    ProcessCode: Optional[str] = Field(None, alias='81', description='')
    NotifyBrokerOfCredit: Optional[bool] = Field(None, alias='208', description='')
    AllocHandlInst: Optional[int] = Field(None, alias='209', description='')
    AllocText: Optional[str] = Field(None, alias='161', description='')
    EncodedAllocTextLen: Optional[int] = Field(None, alias='360', description='')
    EncodedAllocText: Optional[str] = Field(None, alias='361', description='')
    AllocAvgPx: Optional[float] = Field(None, alias='153', description='')
    AllocNetMoney: Optional[float] = Field(None, alias='154', description='')
    SettlCurrAmt: Optional[float] = Field(None, alias='119', description='')
    AllocSettlCurrAmt: Optional[float] = Field(None, alias='737', description='')
    SettlCurrency: Optional[str] = Field(None, alias='120', description='')
    AllocSettlCurrency: Optional[str] = Field(None, alias='736', description='')
    SettlCurrFxRate: Optional[float] = Field(None, alias='155', description='')
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias='156', description='')
    AllocAccruedInterestAmt: Optional[float] = Field(None, alias='742', description='')
    AllocInterestAtMaturity: Optional[float] = Field(None, alias='741', description='')
    AllocSettlInstType: Optional[int] = Field(None, alias='780', description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')
    CommissionData: Optional[CommissionDataComponent] = Field(None, description='')
    MiscFeesGrp: Optional[MiscFeesGrpComponent] = Field(None, description='')
    ClrInstGrp: Optional[ClrInstGrpComponent] = Field(None, description='')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='')



class AllocGrpComponent(FIXComponentBase):
    """FIX Component - AllocGrp"""


