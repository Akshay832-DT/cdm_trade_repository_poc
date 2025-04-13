from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.listordgrp import ListOrdGrp

class NewOrderList(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    listid: str = Field(..., description='', alias='66')
    bidid: Optional[str] = Field(None, description='', alias='390')
    clientbidid: Optional[str] = Field(None, description='', alias='391')
    progrptreqs: Optional[int] = Field(None, description='', alias='414')
    bidtype: int = Field(..., description='', alias='394')
    progperiodinterval: Optional[int] = Field(None, description='', alias='415')
    cancellationrights: Optional[str] = Field(None, description='', alias='480')
    moneylaunderingstatus: Optional[str] = Field(None, description='', alias='481')
    registid: Optional[str] = Field(None, description='', alias='513')
    listexecinsttype: Optional[str] = Field(None, description='', alias='433')
    listexecinst: Optional[str] = Field(None, description='', alias='69')
    encodedlistexecinstlen: Optional[int] = Field(None, description='', alias='352')
    encodedlistexecinst: Optional[str] = Field(None, description='', alias='353')
    allowableonesidednesspct: Optional[float] = Field(None, description='', alias='765')
    allowableonesidednessvalue: Optional[float] = Field(None, description='', alias='766')
    allowableonesidednesscurr: Optional[str] = Field(None, description='', alias='767')
    totnoorders: int = Field(..., description='', alias='68')
    lastfragment: Optional[bool] = Field(None, description='', alias='893')
    listordgrp: ListOrdGrp = Field(..., description='ListOrdGrp component')

