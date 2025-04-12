"""
FIX 4.4 CrossOrderCancelReplaceRequest Message

This module contains the Pydantic model for the CrossOrderCancelReplaceRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructions
from src.models.fix.generated.components.instrmtleggrp import InstrmtLegGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.peginstructions import PegInstructions
from src.models.fix.generated.components.sidecrossordmodgrp import SideCrossOrdModGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class CrossOrderCancelReplaceRequest(FIXMessageBase):
    """
    FIX 4.4 CrossOrderCancelReplaceRequest Message
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
    msgType: Literal["t"] = Field("t", alias='35')
    
    # Message-specific fields
    orderID: Optional[str] = Field(None, description='', alias='37')
    crossID: Optional[str] = Field(None, description='', alias='548')
    origCrossID: Optional[str] = Field(None, description='', alias='551')
    crossType: Optional[int] = Field(None, description='', alias='549')
    crossPrioritization: Optional[int] = Field(None, description='', alias='550')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    handlInst: Optional[str] = Field(None, description='', alias='21')
    execInst: Optional[List[str]] = Field(default_factory=list, description='', alias='18')
    minQty: Optional[float] = Field(None, description='', alias='110')
    maxFloor: Optional[float] = Field(None, description='', alias='111')
    exDestination: Optional[str] = Field(None, description='', alias='100')
    processCode: Optional[str] = Field(None, description='', alias='81')
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    locateReqd: Optional[bool] = Field(None, description='', alias='114')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    ordType: Optional[str] = Field(None, description='', alias='40')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    stopPx: Optional[float] = Field(None, description='', alias='99')
    currency: Optional[str] = Field(None, description='', alias='15')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    iOIID: Optional[str] = Field(None, description='', alias='23')
    quoteID: Optional[str] = Field(None, description='', alias='117')
    timeInForce: Optional[str] = Field(None, description='', alias='59')
    effectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    expireDate: Optional[date] = Field(None, description='', alias='432')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    gTBookingInst: Optional[int] = Field(None, description='', alias='427')
    maxShow: Optional[float] = Field(None, description='', alias='210')
    targetStrategy: Optional[int] = Field(None, description='', alias='847')
    targetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    participationRate: Optional[float] = Field(None, description='', alias='849')
    cancellationRights: Optional[str] = Field(None, description='', alias='480')
    moneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    registID: Optional[str] = Field(None, description='', alias='513')
    designation: Optional[str] = Field(None, description='', alias='494')
    sideCrossOrdModGrp: Optional[SideCrossOrdModGrp] = Field(None, description='SideCrossOrdModGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    instrmtLegGrp: Optional[InstrmtLegGrp] = Field(None, description='InstrmtLegGrp component')
    trdgSesGrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    pegInstructions: Optional[PegInstructions] = Field(None, description='PegInstructions component')
    discretionInstructions: Optional[DiscretionInstructions] = Field(None, description='DiscretionInstructions component')

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
