"""
FIX 4.4 PositionMaintenanceReport Message

This module contains the Pydantic model for the PositionMaintenanceReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.parties import Parties
from ..components.positionamountdata import PositionAmountData
from ..components.positionqty import PositionQty
from ..components.trdgsesgrp import TrdgSesGrp
from ..components.undinstrmtgrp import UndInstrmtGrp


class PositionMaintenanceReport(TradeModel):
    """
    FIX 4.4 PositionMaintenanceReport Message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["AM"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    PosMaintRptID: str = Field(None, description='', alias='721')
    PosTransType: int = Field(None, description='', alias='709')
    PosReqID: Optional[str] = Field(None, description='', alias='710')
    PosMaintAction: int = Field(None, description='', alias='712')
    OrigPosReqRefID: str = Field(None, description='', alias='713')
    PosMaintStatus: int = Field(None, description='', alias='722')
    PosMaintResult: Optional[int] = Field(None, description='', alias='723')
    ClearingBusinessDate: date = Field(None, description='', alias='715')
    SettlSessID: Optional[str] = Field(None, description='', alias='716')
    SettlSessSubID: Optional[str] = Field(None, description='', alias='717')
    Account: str = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: int = Field(None, description='', alias='581')
    Currency: Optional[str] = Field(None, description='', alias='15')
    TransactTime: datetime = Field(None, description='', alias='60')
    AdjustmentType: Optional[int] = Field(None, description='', alias='718')
    ThresholdAmount: Optional[float] = Field(None, description='', alias='834')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[Parties] = None
    Instrument: Instrument = Field(..., description='Instrument component')
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    TrdgSesGrp: Optional[TrdgSesGrp] = None
    PositionQty: PositionQty = Field(..., description='PositionQty component')
    PositionAmountData: PositionAmountData = Field(..., description='PositionAmountData component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"No{field_name[:-1]}"  # Remove 's' from plural
                if no_field in self.__fields__:
                    data[no_field] = len(value)
        
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
