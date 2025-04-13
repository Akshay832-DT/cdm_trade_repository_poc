from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.ordliststatgrp import OrdListStatGrpComponent

class ListStatus(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    ListID: str = Field(..., description='', alias='66')
    ListStatusType: int = Field(..., description='', alias='429')
    NoRpts: int = Field(..., description='', alias='82')
    ListOrderStatus: int = Field(..., description='', alias='431')
    RptSeq: int = Field(..., description='', alias='83')
    ListStatusText: Optional[str] = Field(None, description='', alias='444')
    EncodedListStatusTextLen: Optional[int] = Field(None, description='', alias='445')
    EncodedListStatusText: Optional[str] = Field(None, description='', alias='446')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    TotNoOrders: int = Field(..., description='', alias='68')
    LastFragment: Optional[bool] = Field(None, description='', alias='893')
    OrdListStatGrp: OrdListStatGrpComponent = Field(..., description='OrdListStatGrp component')

