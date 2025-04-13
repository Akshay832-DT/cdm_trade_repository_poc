"""
FIX 4.4 ListOrdGrp Component

This module contains the Pydantic model for the ListOrdGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.preallocgrp import PreAllocGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.peginstructions import PegInstructions
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructions


class NoOrders(FIXMessageBase):
    """
    NoOrders group fields
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
    
    clOrdID: str = Field(..., description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    listSeqNo: int = Field(..., description='', alias='67')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    settlInstMode: Optional[str] = Field(None, description='', alias='160')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    dayBookingInst: Optional[str] = Field(None, description='', alias='589')
    bookingUnit: Optional[str] = Field(None, description='', alias='590')
    allocID: Optional[str] = Field(None, description='', alias='70')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    cashMargin: Optional[str] = Field(None, description='', alias='544')
    clearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    handlInst: Optional[str] = Field(None, description='', alias='21')
    execInst: Optional[List[str]] = Field(None, description='', alias='18')
    minQty: Optional[float] = Field(None, description='', alias='110')
    maxFloor: Optional[float] = Field(None, description='', alias='111')
    exDestination: Optional[str] = Field(None, description='', alias='100')
    processCode: Optional[str] = Field(None, description='', alias='81')
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
    side: str = Field(..., description='', alias='54')
    sideValueInd: Optional[int] = Field(None, description='', alias='401')
    locateReqd: Optional[bool] = Field(None, description='', alias='114')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    ordType: Optional[str] = Field(None, description='', alias='40')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    stopPx: Optional[float] = Field(None, description='', alias='99')
    currency: Optional[str] = Field(None, description='', alias='15')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    solicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    iOIID: Optional[str] = Field(None, description='', alias='23')
    quoteID: Optional[str] = Field(None, description='', alias='117')
    timeInForce: Optional[str] = Field(None, description='', alias='59')
    effectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    expireDate: Optional[date] = Field(None, description='', alias='432')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    gTBookingInst: Optional[int] = Field(None, description='', alias='427')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(None, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    forexReq: Optional[bool] = Field(None, description='', alias='121')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    bookingType: Optional[int] = Field(None, description='', alias='775')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    settlDate2: Optional[date] = Field(None, description='', alias='193')
    orderQty2: Optional[float] = Field(None, description='', alias='192')
    price2: Optional[float] = Field(None, description='', alias='640')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    coveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    maxShow: Optional[float] = Field(None, description='', alias='210')
    targetStrategy: Optional[int] = Field(None, description='', alias='847')
    targetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    participationRate: Optional[float] = Field(None, description='', alias='849')
    designation: Optional[str] = Field(None, description='', alias='494')


class ListOrdGrp(FIXMessageBase):
    """
    FIX 4.4 ListOrdGrp Component
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
    
    parties: Optional[Parties] = Field(None, description='Parties component')
    preAllocGrp: Optional[PreAllocGrp] = Field(None, description='PreAllocGrp component')
    trdgSesGrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')
    instrument: Instrument = Field(..., description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    orderQtyData: OrderQtyData = Field(..., description='OrderQtyData component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
    pegInstructions: Optional[PegInstructions] = Field(None, description='PegInstructions component')
    discretionInstructions: Optional[DiscretionInstructions] = Field(None, description='DiscretionInstructions component')
    noOrders: Optional[int] = Field(None, description='Number of NoOrders entries', alias='73')
    noOrders_items: List[NoOrders] = Field(default_factory=list)
