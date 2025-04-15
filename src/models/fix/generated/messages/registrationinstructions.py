"""FIX message model for RegistrationInstructions (o).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.parties import PartiesComponent
from ..components.rgstdistinstgrp import RgstDistInstGrpComponent
from ..components.rgstdtlsgrp import RgstDtlsGrpComponent

class RegistrationInstructionsMessage(FIXMessageBase):
    """FIX message model for RegistrationInstructions."""

    MsgType: str = Field("o", alias="35")

    RegistID: str = Field(..., alias='513', description='')
    RegistTransType: str = Field(..., alias='514', description='')
    RegistRefID: str = Field(..., alias='508', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    RegistAcctType: Optional[str] = Field(None, alias='493', description='')
    TaxAdvantageType: Optional[int] = Field(None, alias='495', description='')
    OwnershipType: Optional[str] = Field(None, alias='517', description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    RgstDtlsGrp: Optional[RgstDtlsGrpComponent] = Field(None, description='')
    RgstDistInstGrp: Optional[RgstDistInstGrpComponent] = Field(None, description='')

