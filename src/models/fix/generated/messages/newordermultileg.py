"""
FIX 4.4 NewOrderMultileg Message

This module contains the Pydantic model for the NewOrderMultileg message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructions
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.legordgrp import LegOrdGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.peginstructions import PegInstructions
from src.models.fix.generated.components.preallocmleggrp import PreAllocMlegGrp
from src.models.fix.generated.components.trdgsesgrp import TrdgSesGrp
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class NewOrderMultileg(FIXMessageBase):
    """
    FIX 4.4 NewOrderMultileg Message
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
    msgType: Literal["AB"] = Field("AB", alias='35')
    
    # Message-specific fields
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    dayBookingInst: Optional[str] = Field(None, description='', alias='589')
    bookingUnit: Optional[str] = Field(None, description='', alias='590')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    allocID: Optional[str] = Field(None, description='', alias='70')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    cashMargin: Optional[str] = Field(None, description='', alias='544')
    clearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    handlInst: Optional[str] = Field(None, description='', alias='21')
    execInst: Optional[List[str]] = Field(default_factory=list, description='', alias='18')
    minQty: Optional[float] = Field(None, description='', alias='110')
    maxFloor: Optional[float] = Field(None, description='', alias='111')
    exDestination: Optional[str] = Field(None, description='', alias='100')
    processCode: Optional[str] = Field(None, description='', alias='81')
    side: Optional[str] = Field(None, description='', alias='54')
    prevClosePx: Optional[float] = Field(None, description='', alias='140')
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
    orderRestrictions: Optional[List[str]] = Field(default_factory=list, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    forexReq: Optional[bool] = Field(None, description='', alias='121')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    bookingType: Optional[int] = Field(None, description='', alias='775')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    coveredOrUncovered: Optional[int] = Field(None, description='', alias='203')
    maxShow: Optional[float] = Field(None, description='', alias='210')
    targetStrategy: Optional[int] = Field(None, description='', alias='847')
    targetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    participationRate: Optional[float] = Field(None, description='', alias='849')
    cancellationRights: Optional[str] = Field(None, description='', alias='480')
    moneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    registID: Optional[str] = Field(None, description='', alias='513')
    designation: Optional[str] = Field(None, description='', alias='494')
    multiLegRptTypeReq: Optional[int] = Field(None, description='', alias='563')
    parties: Optional[Parties] = Field(None, description='Parties component')
    preAllocMlegGrp: Optional[PreAllocMlegGrp] = Field(None, description='PreAllocMlegGrp component')
    trdgSesGrp: Optional[TrdgSesGrp] = Field(None, description='TrdgSesGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    legOrdGrp: Optional[LegOrdGrp] = Field(None, description='LegOrdGrp component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
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
