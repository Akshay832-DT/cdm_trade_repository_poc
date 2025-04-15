"""
FIX Component Model - SettlInstGrp
"""

from ..base import FIXComponentBase
from .parties import PartiesComponent
from .settlinstructionsdata import SettlInstructionsDataComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoSettlInstGroup(FIXComponentBase):

    """FIX Group - NoSettlInst"""

    SettlInstID: Optional[str] = Field(None, alias='162', description='')
    SettlInstTransType: Optional[str] = Field(None, alias='163', description='')
    SettlInstRefID: Optional[str] = Field(None, alias='214', description='')
    Side: Optional[str] = Field(None, alias='54', description='')
    Product: Optional[int] = Field(None, alias='460', description='')
    SecurityType: Optional[str] = Field(None, alias='167', description='')
    CFICode: Optional[str] = Field(None, alias='461', description='')
    EffectiveTime: Optional[datetime] = Field(None, alias='168', description='')
    ExpireTime: Optional[datetime] = Field(None, alias='126', description='')
    LastUpdateTime: Optional[datetime] = Field(None, alias='779', description='')
    PaymentMethod: Optional[int] = Field(None, alias='492', description='')
    PaymentRef: Optional[str] = Field(None, alias='476', description='')
    CardHolderName: Optional[str] = Field(None, alias='488', description='')
    CardNumber: Optional[str] = Field(None, alias='489', description='')
    CardStartDate: Optional[date] = Field(None, alias='503', description='')
    CardExpDate: Optional[date] = Field(None, alias='490', description='')
    CardIssNum: Optional[str] = Field(None, alias='491', description='')
    PaymentDate: Optional[date] = Field(None, alias='504', description='')
    PaymentRemitterID: Optional[str] = Field(None, alias='505', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    SettlInstructionsData: Optional[SettlInstructionsDataComponent] = Field(None, description='')



class SettlInstGrpComponent(FIXComponentBase):
    """FIX Component - SettlInstGrp"""


