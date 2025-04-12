"""
FIX 4.4 ExecutionReport Message

This module contains the Pydantic model for the ExecutionReport message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.commissiondata import CommissionData
from src.models.fix.generated.components.contamtgrp import ContAmtGrp
from src.models.fix.generated.components.contragrp import ContraGrp
from src.models.fix.generated.components.discretioninstructions import DiscretionInstructions
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrmtlegexecgrp import InstrmtLegExecGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.miscfeesgrp import MiscFeesGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.peginstructions import PegInstructions
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class ExecutionReport(FIXMessageBase):
    """
    FIX 4.4 ExecutionReport Message
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
    msgType: Literal["8"] = Field("8", alias='35')
    
    # Message-specific fields
    orderID: Optional[str] = Field(None, description='', alias='37')
    secondaryOrderID: Optional[str] = Field(None, description='', alias='198')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    secondaryExecID: Optional[str] = Field(None, description='', alias='527')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    origClOrdID: Optional[str] = Field(None, description='', alias='41')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    quoteRespID: Optional[str] = Field(None, description='', alias='693')
    ordStatusReqID: Optional[str] = Field(None, description='', alias='790')
    massStatusReqID: Optional[str] = Field(None, description='', alias='584')
    totNumReports: Optional[int] = Field(None, description='', alias='911')
    lastRptRequested: Optional[bool] = Field(None, description='', alias='912')
    tradeOriginationDate: Optional[date] = Field(None, description='', alias='229')
    listID: Optional[str] = Field(None, description='', alias='66')
    crossID: Optional[str] = Field(None, description='', alias='548')
    origCrossID: Optional[str] = Field(None, description='', alias='551')
    crossType: Optional[int] = Field(None, description='', alias='549')
    execID: Optional[str] = Field(None, description='', alias='17')
    execRefID: Optional[str] = Field(None, description='', alias='19')
    execType: Optional[str] = Field(None, description='', alias='150')
    ordStatus: Optional[str] = Field(None, description='', alias='39')
    workingIndicator: Optional[bool] = Field(None, description='', alias='636')
    ordRejReason: Optional[int] = Field(None, description='', alias='103')
    execRestatementReason: Optional[int] = Field(None, description='', alias='378')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    dayBookingInst: Optional[str] = Field(None, description='', alias='589')
    bookingUnit: Optional[str] = Field(None, description='', alias='590')
    preallocMethod: Optional[str] = Field(None, description='', alias='591')
    settlType: Optional[str] = Field(None, description='', alias='63')
    settlDate: Optional[date] = Field(None, description='', alias='64')
    cashMargin: Optional[str] = Field(None, description='', alias='544')
    clearingFeeIndicator: Optional[str] = Field(None, description='', alias='635')
    side: Optional[str] = Field(None, description='', alias='54')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    ordType: Optional[str] = Field(None, description='', alias='40')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    stopPx: Optional[float] = Field(None, description='', alias='99')
    peggedPrice: Optional[float] = Field(None, description='', alias='839')
    discretionPrice: Optional[float] = Field(None, description='', alias='845')
    targetStrategy: Optional[int] = Field(None, description='', alias='847')
    targetStrategyParameters: Optional[str] = Field(None, description='', alias='848')
    participationRate: Optional[float] = Field(None, description='', alias='849')
    targetStrategyPerformance: Optional[float] = Field(None, description='', alias='850')
    currency: Optional[str] = Field(None, description='', alias='15')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    solicitedFlag: Optional[bool] = Field(None, description='', alias='377')
    timeInForce: Optional[str] = Field(None, description='', alias='59')
    effectiveTime: Optional[datetime] = Field(None, description='', alias='168')
    expireDate: Optional[date] = Field(None, description='', alias='432')
    expireTime: Optional[datetime] = Field(None, description='', alias='126')
    execInst: Optional[List[str]] = Field(default_factory=list, description='', alias='18')
    orderCapacity: Optional[str] = Field(None, description='', alias='528')
    orderRestrictions: Optional[List[str]] = Field(default_factory=list, description='', alias='529')
    custOrderCapacity: Optional[int] = Field(None, description='', alias='582')
    lastQty: Optional[float] = Field(None, description='', alias='32')
    underlyingLastQty: Optional[float] = Field(None, description='', alias='652')
    lastPx: Optional[float] = Field(None, description='', alias='31')
    underlyingLastPx: Optional[float] = Field(None, description='', alias='651')
    lastParPx: Optional[float] = Field(None, description='', alias='669')
    lastSpotRate: Optional[float] = Field(None, description='', alias='194')
    lastForwardPoints: Optional[float] = Field(None, description='', alias='195')
    lastMkt: Optional[str] = Field(None, description='', alias='30')
    tradingSessionID: Optional[str] = Field(None, description='', alias='336')
    tradingSessionSubID: Optional[str] = Field(None, description='', alias='625')
    timeBracket: Optional[str] = Field(None, description='', alias='943')
    lastCapacity: Optional[str] = Field(None, description='', alias='29')
    leavesQty: Optional[float] = Field(None, description='', alias='151')
    cumQty: Optional[float] = Field(None, description='', alias='14')
    avgPx: Optional[float] = Field(None, description='', alias='6')
    dayOrderQty: Optional[float] = Field(None, description='', alias='424')
    dayCumQty: Optional[float] = Field(None, description='', alias='425')
    dayAvgPx: Optional[float] = Field(None, description='', alias='426')
    gTBookingInst: Optional[int] = Field(None, description='', alias='427')
    tradeDate: Optional[date] = Field(None, description='', alias='75')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    reportToExch: Optional[bool] = Field(None, description='', alias='113')
    grossTradeAmt: Optional[float] = Field(None, description='', alias='381')
    numDaysInterest: Optional[int] = Field(None, description='', alias='157')
    exDate: Optional[date] = Field(None, description='', alias='230')
    accruedInterestRate: Optional[float] = Field(None, description='', alias='158')
    accruedInterestAmt: Optional[float] = Field(None, description='', alias='159')
    interestAtMaturity: Optional[float] = Field(None, description='', alias='738')
    endAccruedInterestAmt: Optional[float] = Field(None, description='', alias='920')
    startCash: Optional[float] = Field(None, description='', alias='921')
    endCash: Optional[float] = Field(None, description='', alias='922')
    tradedFlatSwitch: Optional[bool] = Field(None, description='', alias='258')
    basisFeatureDate: Optional[date] = Field(None, description='', alias='259')
    basisFeaturePrice: Optional[float] = Field(None, description='', alias='260')
    concession: Optional[float] = Field(None, description='', alias='238')
    totalTakedown: Optional[float] = Field(None, description='', alias='237')
    netMoney: Optional[float] = Field(None, description='', alias='118')
    settlCurrAmt: Optional[float] = Field(None, description='', alias='119')
    settlCurrency: Optional[str] = Field(None, description='', alias='120')
    settlCurrFxRate: Optional[float] = Field(None, description='', alias='155')
    settlCurrFxRateCalc: Optional[str] = Field(None, description='', alias='156')
    handlInst: Optional[str] = Field(None, description='', alias='21')
    minQty: Optional[float] = Field(None, description='', alias='110')
    maxFloor: Optional[float] = Field(None, description='', alias='111')
    positionEffect: Optional[str] = Field(None, description='', alias='77')
    maxShow: Optional[float] = Field(None, description='', alias='210')
    bookingType: Optional[int] = Field(None, description='', alias='775')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    settlDate2: Optional[date] = Field(None, description='', alias='193')
    orderQty2: Optional[float] = Field(None, description='', alias='192')
    lastForwardPoints2: Optional[float] = Field(None, description='', alias='641')
    multiLegReportingType: Optional[str] = Field(None, description='', alias='442')
    cancellationRights: Optional[str] = Field(None, description='', alias='480')
    moneyLaunderingStatus: Optional[str] = Field(None, description='', alias='481')
    registID: Optional[str] = Field(None, description='', alias='513')
    designation: Optional[str] = Field(None, description='', alias='494')
    transBkdTime: Optional[datetime] = Field(None, description='', alias='483')
    execValuationPoint: Optional[datetime] = Field(None, description='', alias='515')
    execPriceType: Optional[str] = Field(None, description='', alias='484')
    execPriceAdjustment: Optional[float] = Field(None, description='', alias='485')
    priorityIndicator: Optional[int] = Field(None, description='', alias='638')
    priceImprovement: Optional[float] = Field(None, description='', alias='639')
    lastLiquidityInd: Optional[int] = Field(None, description='', alias='851')
    copyMsgIndicator: Optional[bool] = Field(None, description='', alias='797')
    parties: Optional[Parties] = Field(None, description='Parties component')
    contraGrp: Optional[ContraGrp] = Field(None, description='ContraGrp component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    pegInstructions: Optional[PegInstructions] = Field(None, description='PegInstructions component')
    discretionInstructions: Optional[DiscretionInstructions] = Field(None, description='DiscretionInstructions component')
    commissionData: Optional[CommissionData] = Field(None, description='CommissionData component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')
    contAmtGrp: Optional[ContAmtGrp] = Field(None, description='ContAmtGrp component')
    instrmtLegExecGrp: Optional[InstrmtLegExecGrp] = Field(None, description='InstrmtLegExecGrp component')
    miscFeesGrp: Optional[MiscFeesGrp] = Field(None, description='MiscFeesGrp component')

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
