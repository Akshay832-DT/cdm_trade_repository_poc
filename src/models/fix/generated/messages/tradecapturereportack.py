"""
FIX 4.4 TradeCaptureReportAck Message

This module contains the Pydantic model for the TradeCaptureReportAck message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrument import Instrument
from ..components.trdallocgrp import TrdAllocGrp
from ..components.trdinstrmtleggrp import TrdInstrmtLegGrp
from ..components.trdregtimestamps import TrdRegTimestamps


class TradeCaptureReportAck(TradeModel):
    """
    FIX 4.4 TradeCaptureReportAck Message
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
    MsgType: Literal["AR"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    TradeReportID: str = Field(None, description='', alias='571')
    TradeReportTransType: Optional[int] = Field(None, description='', alias='487')
    TradeReportType: Optional[int] = Field(None, description='', alias='856')
    TrdType: Optional[int] = Field(None, description='', alias='828')
    TrdSubType: Optional[int] = Field(None, description='', alias='829')
    SecondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    TransferReason: Optional[str] = Field(None, description='', alias='830')
    ExecType: str = Field(None, description='', alias='150')
    TradeReportRefID: Optional[str] = Field(None, description='', alias='572')
    SecondaryTradeReportRefID: Optional[str] = Field(None, description='', alias='881')
    TrdRptStatus: Optional[int] = Field(None, description='', alias='939')
    TradeReportRejectReason: Optional[int] = Field(None, description='', alias='751')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TradeLinkID: Optional[str] = Field(None, description='', alias='820')
    TrdMatchID: Optional[str] = Field(None, description='', alias='880')
    ExecID: Optional[str] = Field(None, description='', alias='17')
    SecondaryExecID: Optional[str] = Field(None, description='', alias='527')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    ClearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    OrderCapacity: Optional[str] = Field(None, description='', alias='528')
    OrderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    CustOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    AccountType: Optional[int] = Field(None, description='', alias='581')
    PositionEffect: Optional[str] = Field(None, description='', alias='77')
    PreallocMethod: Optional[str] = Field(None, description='', alias='591')
    Instrument: Instrument = Field(..., description='Instrument component')
    TrdRegTimestamps: Optional[TrdRegTimestamps] = None
    TrdInstrmtLegGrp: Optional[TrdInstrmtLegGrp] = None
    TrdAllocGrp: Optional[TrdAllocGrp] = None

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
