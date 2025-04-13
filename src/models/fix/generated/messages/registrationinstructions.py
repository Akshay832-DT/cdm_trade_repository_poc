from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.rgstdtlsgrp import RgstDtlsGrp
from src.models.fix.generated.components.rgstdistinstgrp import RgstDistInstGrp

class RegistrationInstructions(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    registid: str = Field(..., description='', alias='513')
    registtranstype: str = Field(..., description='', alias='514')
    registrefid: str = Field(..., description='', alias='508')
    clordid: Optional[str] = Field(None, description='', alias='11')
    account: Optional[str] = Field(None, description='', alias='1')
    acctidsource: Optional[int] = Field(None, description='', alias='660')
    registaccttype: Optional[str] = Field(None, description='', alias='493')
    taxadvantagetype: Optional[int] = Field(None, description='', alias='495')
    ownershiptype: Optional[str] = Field(None, description='', alias='517')
    parties: Optional[Parties] = Field(None, description='Parties component')
    rgstdtlsgrp: Optional[RgstDtlsGrp] = Field(None, description='RgstDtlsGrp component')
    rgstdistinstgrp: Optional[RgstDistInstGrp] = Field(None, description='RgstDistInstGrp component')

