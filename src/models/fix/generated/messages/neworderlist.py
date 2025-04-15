"""FIX message model for NewOrderList (E).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.listordgrp import ListOrdGrpComponent

class NewOrderListMessage(FIXMessageBase):
    """FIX message model for NewOrderList."""

    MsgType: str = Field("E", alias="35")

    ListID: str = Field(..., alias='66', description='')
    BidID: Optional[str] = Field(None, alias='390', description='')
    ClientBidID: Optional[str] = Field(None, alias='391', description='')
    ProgRptReqs: Optional[int] = Field(None, alias='414', description='')
    BidType: int = Field(..., alias='394', description='')
    ProgPeriodInterval: Optional[int] = Field(None, alias='415', description='')
    CancellationRights: Optional[str] = Field(None, alias='480', description='')
    MoneyLaunderingStatus: Optional[str] = Field(None, alias='481', description='')
    RegistID: Optional[str] = Field(None, alias='513', description='')
    ListExecInstType: Optional[str] = Field(None, alias='433', description='')
    ListExecInst: Optional[str] = Field(None, alias='69', description='')
    EncodedListExecInstLen: Optional[int] = Field(None, alias='352', description='')
    EncodedListExecInst: Optional[str] = Field(None, alias='353', description='')
    AllowableOneSidednessPct: Optional[float] = Field(None, alias='765', description='')
    AllowableOneSidednessValue: Optional[float] = Field(None, alias='766', description='')
    AllowableOneSidednessCurr: Optional[str] = Field(None, alias='767', description='')
    TotNoOrders: int = Field(..., alias='68', description='')
    LastFragment: Optional[bool] = Field(None, alias='893', description='')
    ListOrdGrp: ListOrdGrpComponent = Field(..., description='')

