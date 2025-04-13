from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.listordgrp import ListOrdGrpComponent

class NewOrderList(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ListID: str = Field(..., description='', alias='66')
    BidID: Optional[str] = Field(None, description='', alias='390')
    ClientBidID: Optional[str] = Field(None, description='', alias='391')
    ProgRptReqs: Optional[int] = Field(None, description='', alias='414')
    BidType: int = Field(..., description='', alias='394')
    ProgPeriodInterval: Optional[int] = Field(None, description='', alias='415')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    ListExecInstType: Optional[str] = Field(None, description='', alias='433')
    ListExecInst: Optional[str] = Field(None, description='', alias='69')
    EncodedListExecInstLen: Optional[int] = Field(None, description='', alias='352')
    EncodedListExecInst: Optional[str] = Field(None, description='', alias='353')
    AllowableOneSidednessPct: Optional[float] = Field(None, description='', alias='765')
    AllowableOneSidednessValue: Optional[float] = Field(None, description='', alias='766')
    AllowableOneSidednessCurr: Optional[str] = Field(None, description='', alias='767')
    TotNoOrders: int = Field(..., description='', alias='68')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    ListOrdGrp: ListOrdGrpComponent = Field(..., description='ListOrdGrp component')

