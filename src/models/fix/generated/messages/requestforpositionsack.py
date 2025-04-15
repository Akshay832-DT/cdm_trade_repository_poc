"""FIX message model for RequestForPositionsAck (AO).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class RequestForPositionsAckMessage(FIXMessageBase):
    """FIX message model for RequestForPositionsAck."""

    MsgType: str = Field("AO", alias="35")

    PosMaintRptID: str = Field(..., alias='721', description='')
    PosReqID: Optional[str] = Field(None, alias='710', description='')
    TotalNumPosReports: Optional[int] = Field(None, alias='727', description='')
    UnsolicitedIndicator: Optional[bool] = Field(None, alias='325', description='')
    PosReqResult: int = Field(..., alias='728', description='')
    PosReqStatus: int = Field(..., alias='729', description='')
    Account: str = Field(..., alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: PartiesComponent = Field(..., description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')

