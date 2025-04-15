"""FIX message model for PositionMaintenanceRequest (AL).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.instrmtleggrp import InstrmtLegGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.parties import PartiesComponent
from ..components.positionqty import PositionQtyComponent
from ..components.trdgsesgrp import TrdgSesGrpComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent

class PositionMaintenanceRequestMessage(FIXMessageBase):
    """FIX message model for PositionMaintenanceRequest."""

    MsgType: str = Field("AL", alias="35")

    PosReqID: str = Field(..., alias='710', description='')
    PosTransType: int = Field(..., alias='709', description='')
    PosMaintAction: int = Field(..., alias='712', description='')
    OrigPosReqRefID: Optional[str] = Field(None, alias='713', description='')
    PosMaintRptRefID: Optional[str] = Field(None, alias='714', description='')
    ClearingBusinessDate: date = Field(..., alias='715', description='')
    SettlSessID: Optional[str] = Field(None, alias='716', description='')
    SettlSessSubID: Optional[str] = Field(None, alias='717', description='')
    Account: str = Field(..., alias='1', description='')
    AcctIDSource: Optional[int] = Field(None, alias='660', description='')
    AccountType: int = Field(..., alias='581', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    TransactTime: datetime = Field(..., alias='60', description='')
    AdjustmentType: Optional[int] = Field(None, alias='718', description='')
    ContraryInstructionIndicator: Optional[bool] = Field(None, alias='719', description='')
    PriorSpreadIndicator: Optional[bool] = Field(None, alias='720', description='')
    ThresholdAmount: Optional[float] = Field(None, alias='834', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    Parties: PartiesComponent = Field(..., description='')
    Instrument: InstrumentComponent = Field(..., description='')
    InstrmtLegGrp: Optional[InstrmtLegGrpComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    TrdgSesGrp: Optional[TrdgSesGrpComponent] = Field(None, description='')
    PositionQty: PositionQtyComponent = Field(..., description='')

