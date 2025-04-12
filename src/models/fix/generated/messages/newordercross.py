"""
FIX 4.4 NewOrderCross Message

This module contains the Pydantic model for the NewOrderCross message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.discretioninstructions import DiscretionInstructions
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.instrument import Instrument
from ..components.peginstructions import PegInstructions
from ..components.sidecrossordmodgrp import SideCrossOrdModGrp
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.trdgsesgrp import TrdgSesGrp
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class NewOrderCross(TradeModel):
    """
    FIX 4.4 NewOrderCross Message
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
    MsgType: Literal["s"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    CrossID: str = Field(None, description='', alias='548')
    CrossType: int = Field(None, description='', alias='549')
    CrossPrioritization: int = Field(None, description='', alias='550')
    SettlType: Optional[str] = Field(None, description='', alias='63')
    SettlDate: Optional[date] = Field(None, description='', alias='64')
    HandlInst: Optional[str] = Field(None, description='', alias='21')
    ExecInst: Optional[List[str]] = Field(None, description='', alias='18')
    MinQty: Optional[float] = Field(None, description='', alias='110')
    MaxFloor: Optional[float] = Field(None, description='', alias='111')
    ExDestination: Optional[str] = Field(None, description='', alias='100')
    ProcessCode: Optional[str] = Field(None, description='', alias='81')
    PrevClosePx: Optional[float] = Field(None, description='', alias='140')
    LocateReqd: Optional[bool] = Field(None, description='', alias='114')
    TransactTime: datetime = Field(None, description='', alias='60')
    OrdType: str = Field(None, description='', alias='40')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    StopPx: Optional[float] = Field(None, description='', alias='99')
    Currency: Optional[str] = Field(None, description='', alias='15')
    ComplianceID: Optional[str] = Field(None, description='', alias='376')
    IOIID: Optional[str] = Field(None, description='', alias='23')
    QuoteID: Optional[str] = Field(None, description='', alias='117')
    TimeInForce: Optional[str] = Field(None, description='', alias='59')
    EffectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    ExpireDate: Optional[date] = Field(None, description='', alias='432')
    ExpireTime: Optional[datetime] = Field(None, description='', alias='126')
    GTBookingInst: Optional[int] = Field(None, description='', alias='427')
    MaxShow: Optional[float] = Field(None, description='', alias='210')
    TargetStrategy: Optional[int] = Field(None, description='', alias='847')
    TargetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    ParticipationRate: Optional[float] = Field(None, description='', alias='849')
    CancellationRights: Optional[str] = Field(None, description='', alias='480')
    MoneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    RegistID: Optional[str] = Field(None, description='', alias='513')
    Designation: Optional[str] = Field(None, description='', alias='494')
    SideCrossOrdModGrp: SideCrossOrdModGrp = Field(..., description='SideCrossOrdModGrp component')
    Instrument: Instrument = Field(..., description='Instrument component')
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    TrdgSesGrp: Optional[TrdgSesGrp] = None
    Stipulations: Optional[Stipulations] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    YieldData: Optional[YieldData] = None
    PegInstructions: Optional[PegInstructions] = None
    DiscretionInstructions: Optional[DiscretionInstructions] = None

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
