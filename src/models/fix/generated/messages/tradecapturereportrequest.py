"""
FIX 4.4 TradeCaptureReportRequest Message

This module contains the Pydantic model for the TradeCaptureReportRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.instrumentextension import InstrumentExtension
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.trdcapdtgrp import TrdCapDtGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class TradeCaptureReportRequest(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["AD"] = Field("AD", alias='35')
    
    # Message-specific fields
    tradeRequestID: Optional[str] = Field(None, description='', alias='568')
    tradeRequestType: Optional[int] = Field(None, description='', alias='569')
    subscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    tradeReportID: Optional[str] = Field(None, description='', alias='571')
    secondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    execID: Optional[str] = Field(None, description='', alias='17')
    execType: Optional[str] = Field(None, description='', alias='150')
    orderID: Optional[str] = Field(None, description='', alias='37')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    matchStatus: Optional[str] = Field(None, description='', alias='573')
    trdType: Optional[int] = Field(None, description='', alias='828')
    trdSubType: Optional[int] = Field(None, description='', alias='829')
    transferReason: Optional[str] = Field(None, description='', alias='830')
    secondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    tradeLinkID: Optional[str] = Field(None, description='', alias='820')
    trdMatchID: Optional[str] = Field(None, description='', alias='880')
    clearingBusinessDate: Optional[date] = Field(None, description='', alias='715')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    timeBracket: Optional[str] = Field(None, description='', alias='943')
    side: Optional[str] = Field(None, description='', alias='54')
    multiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    tradeInputSource: Optional[str] = Field(None, description='', alias='578')
    tradeInputDevice: Optional[str] = Field(None, description='', alias='579')
    responseTransportType: Optional[int] = Field(None, description='', alias='725')
    responseDestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    instrumentExtension: Optional[InstrumentExtension] = Field(None, description='InstrumentExtension component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    trdCapDtGrp: Optional[TrdCapDtGrp] = Field(None, description='TrdCapDtGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
