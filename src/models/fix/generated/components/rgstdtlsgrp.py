"""
FIX 4.4 RgstDtlsGrp Component

This module contains the Pydantic model for the RgstDtlsGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class RgstDtlsGrp(FIXMessageBase):
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
    registDtls: Optional[str] = Field(None, description='', alias='509')
    registEmail: Optional[str] = Field(None, description='', alias='511')
    mailingDtls: Optional[str] = Field(None, description='', alias='474')
    mailingInst: Optional[str] = Field(None, description='', alias='482')
    ownerType: Optional[int] = Field(None, description='', alias='522')
    dateOfBirth: Optional[date] = Field(None, description='', alias='486')
    investorCountryOfResidence: Optional[str] = Field(None, description='', alias='475')
    nestedParties: Optional[str] = Field(None)


class NoRegistDtls(FIXMessageBase):
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
    registDtls: Optional[int] = Field(None, description='', alias='473')
    registEmail: Optional[int] = Field(None, description='', alias='473')
    mailingDtls: Optional[int] = Field(None, description='', alias='473')
    mailingInst: Optional[int] = Field(None, description='', alias='473')
    ownerType: Optional[int] = Field(None, description='', alias='473')
    dateOfBirth: Optional[int] = Field(None, description='', alias='473')
    investorCountryOfResidence: Optional[int] = Field(None, description='', alias='473')

    noRegistDtlss: List[NoRegistDtls] = Field(default_factory=list)
