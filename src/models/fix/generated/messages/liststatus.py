from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordliststatgrp import OrdListStatGrp

class ListStatus(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    listid: str = Field(..., description='', alias='66')
    liststatustype: int = Field(..., description='', alias='429')
    norpts: int = Field(..., description='', alias='82')
    listorderstatus: int = Field(..., description='', alias='431')
    rptseq: int = Field(..., description='', alias='83')
    liststatustext: Optional[str] = Field(None, description='', alias='444')
    encodedliststatustextlen: Optional[int] = Field(None, description='', alias='445')
    encodedliststatustext: Optional[str] = Field(None, description='', alias='446')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    totnoorders: int = Field(..., description='', alias='68')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    ordliststatgrp: OrdListStatGrp = Field(..., description='OrdListStatGrp component')

