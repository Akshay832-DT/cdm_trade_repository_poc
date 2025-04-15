"""
FIX Component Model - RgstDtlsGrp
"""

from ..base import FIXComponentBase
from .nestedparties import NestedPartiesComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoRegistDtlsGroup(FIXComponentBase):

    """FIX Group - NoRegistDtls"""

    RegistDtls: Optional[str] = Field(None, alias='509', description='')
    RegistEmail: Optional[str] = Field(None, alias='511', description='')
    MailingDtls: Optional[str] = Field(None, alias='474', description='')
    MailingInst: Optional[str] = Field(None, alias='482', description='')
    OwnerType: Optional[int] = Field(None, alias='522', description='')
    DateOfBirth: Optional[date] = Field(None, alias='486', description='')
    InvestorCountryOfResidence: Optional[str] = Field(None, alias='475', description='')
    NestedParties: Optional[NestedPartiesComponent] = Field(None, description='')



class RgstDtlsGrpComponent(FIXComponentBase):
    """FIX Component - RgstDtlsGrp"""


