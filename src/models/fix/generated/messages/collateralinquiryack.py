from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.collinqqualgrp import CollInqQualGrpComponent
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.execcollgrp import ExecCollGrpComponent
from src.models.fix.generated.components.trdcollgrp import TrdCollGrpComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent

class CollateralInquiryAck(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    CollInquiryID: str = Field(..., description='', alias='909')
    CollInquiryStatus: int = Field(..., description='', alias='945')
    CollInquiryResult: Optional[int] = Field(None, description='', alias='946')
    TotNumReports: Optional[int] = Field(None, description='', alias='911')
    Account: Optional[str] = Field(None, description='', alias='1')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    SecondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    SecondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    Quantity: Optional[float] = Field(None, description='', alias='53')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    CollInqQualGrp: Optional[CollInqQualGrpComponent] = Field(None, description='CollInqQualGrp component')
    Parties: Optional[PartiesComponent] = Field(None, description='Parties component')
    ExecCollGrp: Optional[ExecCollGrpComponent] = Field(None, description='ExecCollGrp component')
    TrdCollGrp: Optional[TrdCollGrpComponent] = Field(None, description='TrdCollGrp component')
    Instrument: Optional[InstrumentComponent] = Field(None, description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')

