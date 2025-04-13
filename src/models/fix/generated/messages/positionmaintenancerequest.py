from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import PartiesComponent
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrpComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrpComponent
from src.models.fix.generated.components.positionqty import PositionQtyComponent

class PositionMaintenanceRequest(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    PosReqID: str = Field(..., description='', alias='710')
    PosTransType: int = Field(..., description='', alias='709')
    PosMaintAction: int = Field(..., description='', alias='712')
    OrigPosReqRefID: Optional[str] = Field(None, description='', alias='713')
    PosMaintRptRefID: Optional[str] = Field(None, description='', alias='714')
    ClearingBusinessDate: date = Field(..., description='', alias='715')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    Account: str = Field(..., description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: int = Field(..., description='', alias='581')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TransactTime: datetime = Field(..., description='', alias='60')
    AdjustmentType: Optional[int] = Field(None, description='', alias='718')
    ContraryInstructionIndicator: Optional[bool] = Field(None, description='', alias='719')
    PriorSpreadIndicator: Optional[bool] = Field(None, description='', alias='720')
    ThresholdAmount: Optional[float] = Field(None, description='', alias='834')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: PartiesComponent = Field(..., description='Parties component')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='InstrmtLegGrp component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='TrdgSesGrp component')
    PositionQty: PositionQtyComponent = Field(..., description='PositionQty component')

