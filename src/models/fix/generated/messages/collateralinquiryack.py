"""FIX message model for CollateralInquiryAck (BG).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.collinqqualgrp import CollInqQualGrpComponent
from ..components.execcollgrp import ExecCollGrpComponent
from ..components.financingdetails import FinancingDetailsComponent
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.trdcollgrp import TrdCollGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class CollateralInquiryAckMessage(FIXMessageBase):
    """FIX message model for CollateralInquiryAck."""

    MsgType: str = Field("BG", alias="35")

    CollInquiryID: str = Field(..., alias='909', description='')
    CollInquiryStatus: int = Field(..., alias='945', description='')
    CollInquiryResult: Optional[int] = Field(None, alias='946', description='')
    TotNumReports: Optional[int] = Field(None, alias='911', description='')
    Account: Optional[str] = Field(None, alias='1', description='')
    AccountType: Optional[int] = Field(None, alias='581', description='')
    ClOrdID: Optional[str] = Field(None, alias='11', description='')
    OrderID: Optional[str] = Field(None, alias='37', description='')
    SecondaryOrderID: Optional[str] = Field(None, alias='198', description='')
    SecondaryClOrdID: Optional[str] = Field(None, alias='526', description='')
    SettlDate: Optional[date] = Field(None, alias='64', description='')
    Quantity: Optional[float] = Field(None, alias='53', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    TradingSessionID: Optional[str] = Field(None, alias='336', description='')
    TradingSessionSubID: Optional[str] = Field(None, alias='625', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    ClearingBusinessDate: Optional[date] = Field(None, alias='715', description='')
    ResponseTransportType: Optional[int] = Field(None, alias='725', description='')
    ResponseDestination: Optional[str] = Field(None, alias='726', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    CollInqQualGrp: Optional[CollInqQualGrpComponent] = Field(None, description='')
    Parties: Optional[PartiesComponent] = Field(None, description='')
    ExecCollGrp: Optional[ExecCollGrpComponent] = Field(None, description='')
    TrdCollGrp: Optional[TrdCollGrpComponent] = Field(None, description='')
    Instrument: Optional[InstrumentComponent] = Field(None, description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')

