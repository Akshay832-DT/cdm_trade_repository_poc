"""
FIX 4.4 TradeCaptureReportAck Message

This module contains the Pydantic model for the TradeCaptureReportAck message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.trdallocgrp import TrdAllocGrp
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps


class TradeCaptureReportAck(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["AR"] = Field("AR", alias='35')
    
    # Message-specific fields
    tradeReportID: Optional[str] = Field(None, description='', alias='571')
    tradeReportTransType: Optional[int] = Field(None, description='', alias='487')
    tradeReportType: Optional[int] = Field(None, description='', alias='856')
    trdType: Optional[int] = Field(None, description='', alias='828')
    trdSubType: Optional[int] = Field(None, description='', alias='829')
    secondaryTrdType: Optional[int] = Field(None, description='', alias='855')
    transferReason: Optional[str] = Field(None, description='', alias='830')
    execType: Optional[str] = Field(None, description='', alias='150')
    tradeReportRefID: Optional[str] = Field(None, description='', alias='572')
    secondaryTradeReportRefID: Optional[str] = Field(None, description='', alias='881')
    trdRptStatus: Optional[int] = Field(None, description='', alias='939')
    tradeReportRejectReason: Optional[int] = Field(None, description='', alias='751')
    secondaryTradeReportID: Optional[str] = Field(None, description='', alias='818')
    subscriptionRequestType: Optional[str] = Field(None, description='', alias='263')
    tradeLinkID: Optional[str] = Field(None, description='', alias='820')
    trdMatchID: Optional[str] = Field(None, description='', alias='880')
    execID: Optional[str] = Field(None, description='', alias='17')
    secondaryExecID: Optional[str] = Field(None, description='', alias='527')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    responseTransportType: Optional[int] = Field(None, description='', alias='725')
    responseDestination: Optional[str] = Field(None, description='', alias='726')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    clearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(default_factory=list, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    trdRegTimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    trdInstrmtLegGrp: Optional[TrdInstrmtLegGrp] = Field(None, description='TrdInstrmtLegGrp component')
    trdAllocGrp: Optional[TrdAllocGrp] = Field(None, description='TrdAllocGrp component')

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
