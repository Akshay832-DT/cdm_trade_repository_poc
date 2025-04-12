"""
FIX 4.4 TradeCaptureReportRequest Message

This module contains the Pydantic model for the TradeCaptureReportRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.financingdetails import FinancingDetails
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.instrumentextension import InstrumentExtension
from ..components.parties import Parties
from ..components.trdcapdtgrp import TrdCapDtGrp
from ..components.undinstrmtgrp import UndInstrmtGrp


class TradeCaptureReportRequest(TradeModel):
    """
    FIX 4.4 TradeCaptureReportRequest Message
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
    MsgType: Literal["AD"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    TradeRequestID: str = Field(None, description='', alias='568')
    TradeRequestType: int = Field(None, description='', alias='569')
    SubscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    TradeReportID: Optional[str] = Field(None, description='', alias='571')
    SecondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    ExecID: Optional[str] = Field(None, description='', alias='17')
    ExecType: Optional[str] = Field(None, description='', alias='150')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    MatchStatus: Optional[str] = Field(None, description='', alias='573')
    TrdType: Optional[int] = Field(None, description='', alias='828')
    TrdSubType: Optional[int] = Field(None, description='', alias='829')
    TransferReason: Optional[str] = Field(None, description='', alias='830')
    SecondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    TradeLinkID: Optional[str] = Field(None, description='', alias='820')
    TrdMatchID: Optional[str] = Field(None, description='', alias='880')
    ClearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    TradingSessionID: Optional[str] = Field(None, description='', alias='336')
    TradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    TimeBracket: Optional[str] = Field(None, description='', alias='943')
    Side: Optional[str] = Field(None, description='', alias='54')
    MultiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    TradeInputSource: Optional[str] = Field(None, description='', alias='578')
    TradeInputDevice: Optional[str] = Field(None, description='', alias='579')
    ResponseTransportType: Optional[int] = Field(None, description='', alias='725')
    ResponseDestination: Optional[str] = Field(None, description='', alias='726')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    Parties: Optional[Parties] = None
    Instrument: Optional[Instrument] = None
    InstrumentExtension: Optional[InstrumentExtension] = None
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    TrdCapDtGrp: Optional[TrdCapDtGrp] = None

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
