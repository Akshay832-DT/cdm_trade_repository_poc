"""
FIX 4.4 RgstDtlsGrp Component

This module contains the Pydantic model for the RgstDtlsGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoRegistDtlsGroup(FIXComponentBase):
    """
    NoRegistDtls group fields
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
    
    RegistDtls: Optional[str] = Field(None, description='', alias='509')
    RegistEmail: Optional[str] = Field(None, description='', alias='511')
    MailingDtls: Optional[str] = Field(None, description='', alias='474')
    MailingInst: Optional[str] = Field(None, description='', alias='482')
    OwnerType: Optional[int] = Field(None, description='', alias='522')
    DateOfBirth: Optional[date] = Field(None, description='', alias='486')
    InvestorCountryOfResidence: Optional[str] = Field(None, description='', alias='475')


class RgstDtlsGrpComponent(FIXComponentBase):
    """
    FIX 4.4 RgstDtlsGrp Component
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
    NoRegistDtls: Optional[int] = Field(None, description='Number of NoRegistDtls entries', alias='')
    NoRegistDtls_items: List[NoRegistDtlsGroup] = Field(default_factory=list)
