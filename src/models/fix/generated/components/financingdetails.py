"""
FIX Component Model - FinancingDetails
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class FinancingDetailsComponent(FIXComponentBase):
    """FIX Component - FinancingDetails"""
    AgreementDesc: Optional[str] = Field(None, alias='913', description='')
    AgreementID: Optional[str] = Field(None, alias='914', description='')
    AgreementDate: Optional[date] = Field(None, alias='915', description='')
    AgreementCurrency: Optional[str] = Field(None, alias='918', description='')
    TerminationType: Optional[int] = Field(None, alias='788', description='')
    StartDate: Optional[date] = Field(None, alias='916', description='')
    EndDate: Optional[date] = Field(None, alias='917', description='')
    DeliveryType: Optional[int] = Field(None, alias='919', description='')
    MarginRatio: Optional[float] = Field(None, alias='898', description='')

