"""
FIX 4.4 ListOrdGrp Component

This module contains the Pydantic model for the ListOrdGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


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
    clOrdID: str = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    listSeqNo: int = Field(None, description='', alias='67')
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
    side: str = Field(None, description='', alias='54')
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
    parties: Optional[str] = Field(None)
    preAllocGrp: Optional[str] = Field(None)
    trdgSesGrp: Optional[str] = Field(None)
    instrument: str = Field(None)
    undInstrmtGrp: Optional[str] = Field(None)
    stipulations: Optional[str] = Field(None)
    orderQtyData: str = Field(None)
    spreadOrBenchmarkCurveData: Optional[str] = Field(None)
    yieldData: Optional[str] = Field(None)
    commissionData: Optional[str] = Field(None)
    pegInstructions: Optional[str] = Field(None)
    discretionInstructions: Optional[str] = Field(None)


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
    clOrdID: int = Field(None, description='', alias='73')
    secondaryClOrdID: Optional[int] = Field(None, description='', alias='73')
    listSeqNo: int = Field(None, description='', alias='73')
    clOrdLinkID: Optional[int] = Field(None, description='', alias='73')
    settlInstMode: Optional[int] = Field(None, description='', alias='73')
    tradeOriginationDate: Optional[int] = Field(None, description='', alias='73')
    tradeDate: Optional[int] = Field(None, description='', alias='73')
    account: Optional[int] = Field(None, description='', alias='73')
    acctIDSource: Optional[int] = Field(None, description='', alias='73')
    accountType: Optional[int] = Field(None, description='', alias='73')
    dayBookingInst: Optional[int] = Field(None, description='', alias='73')
    bookingUnit: Optional[int] = Field(None, description='', alias='73')
    allocID: Optional[int] = Field(None, description='', alias='73')
    preallocMethod: Optional[int] = Field(None, description='', alias='73')
    settlType: Optional[int] = Field(None, description='', alias='73')
    settlDate: Optional[int] = Field(None, description='', alias='73')
    cashMargin: Optional[int] = Field(None, description='', alias='73')
    clearingFeeIndicator: Optional[int] = Field(None, description='', alias='73')
    handlInst: Optional[int] = Field(None, description='', alias='73')
    execInst: Optional[int] = Field(None, description='', alias='73')
    minQty: Optional[int] = Field(None, description='', alias='73')
    maxFloor: Optional[int] = Field(None, description='', alias='73')
    exDestination: Optional[int] = Field(None, description='', alias='73')
    processCode: Optional[int] = Field(None, description='', alias='73')
    prevClosePx: Optional[int] = Field(None, description='', alias='73')
    side: int = Field(None, description='', alias='73')
    sideValueInd: Optional[int] = Field(None, description='', alias='73')
    locateReqd: Optional[int] = Field(None, description='', alias='73')
    transactTime: Optional[int] = Field(None, description='', alias='73')
    qtyType: Optional[int] = Field(None, description='', alias='73')
    ordType: Optional[int] = Field(None, description='', alias='73')
    priceType: Optional[int] = Field(None, description='', alias='73')
    price: Optional[int] = Field(None, description='', alias='73')
    stopPx: Optional[int] = Field(None, description='', alias='73')
    currency: Optional[int] = Field(None, description='', alias='73')
    complianceID: Optional[int] = Field(None, description='', alias='73')
    solicitedFlag: Optional[int] = Field(None, description='', alias='73')
    iOIID: Optional[int] = Field(None, description='', alias='73')
    quoteID: Optional[int] = Field(None, description='', alias='73')
    timeInForce: Optional[int] = Field(None, description='', alias='73')
    effectiveTime: Optional[int] = Field(None, description='', alias='73')
    expireDate: Optional[int] = Field(None, description='', alias='73')
    expireTime: Optional[int] = Field(None, description='', alias='73')
    gTBookingInst: Optional[int] = Field(None, description='', alias='73')
    orderCapacity: Optional[int] = Field(None, description='', alias='73')
    orderRestrictions: Optional[int] = Field(None, description='', alias='73')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='73')
    forexReq: Optional[int] = Field(None, description='', alias='73')
    settlCurrency: Optional[int] = Field(None, description='', alias='73')
    bookingType: Optional[int] = Field(None, description='', alias='73')
    text: Optional[int] = Field(None, description='', alias='73')
    encodedTextLen: Optional[int] = Field(None, description='', alias='73')
    encodedText: Optional[int] = Field(None, description='', alias='73')
    settlDate2: Optional[int] = Field(None, description='', alias='73')
    orderQty2: Optional[int] = Field(None, description='', alias='73')
    price2: Optional[int] = Field(None, description='', alias='73')
    positionEffect: Optional[int] = Field(None, description='', alias='73')
    coveredOrUncovered: Optional[int] = Field(None, description='', alias='73')
    maxShow: Optional[int] = Field(None, description='', alias='73')
    targetStrategy: Optional[int] = Field(None, description='', alias='73')
    targetStrategyParameters: Optional[int] = Field(None, description='', alias='73')
    participationRate: Optional[int] = Field(None, description='', alias='73')
    designation: Optional[int] = Field(None, description='', alias='73')

    noOrderss: List[NoOrders] = Field(default_factory=list)
