"""
FIX Component Model - CommissionData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class CommissionDataComponent(FIXComponentBase):
    """FIX Component - CommissionData"""
    Commission: Optional[float] = Field(None, alias='12', description='')
    CommType: Optional[str] = Field(None, alias='13', description='')
    CommCurrency: Optional[str] = Field(None, alias='479', description='')
    FundRenewWaiv: Optional[str] = Field(None, alias='497', description='')

