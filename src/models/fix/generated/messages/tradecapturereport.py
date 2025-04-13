from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.yielddata import YieldData
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.positionamountdata import PositionAmountData
from src.models.fix.generated.components.trdinstrmtleggrp import TrdInstrmtLegGrp
from src.models.fix.generated.components.trdregtimestamps import TrdRegTimestamps
from src.models.fix.generated.components.trdcaprptsidegrp import TrdCapRptSideGrp

class TradeCaptureReport(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    tradereportid: str = Field(..., description='', alias='571')
    tradereporttranstype: Optional[int] = Field(None, description='', alias='487')
    tradereporttype: Optional[int] = Field(None, description='', alias='856')
    traderequestid: Optional[str] = Field(None, description='', alias='568')
    trdtype: Optional[int] = Field(None, description='', alias='828')
    trdsubtype: Optional[int] = Field(None, description='', alias='829')
    secondarytrdtype: Optional[int] = Field(None, description='', alias='855')
    transferreason: Optional[str] = Field(None, description='', alias='830')
    exectype: Optional[str] = Field(None, description='', alias='150')
    totnumtradereports: Optional[int] = Field(None, description='', alias='748')
    lastrptrequested: Optional[bool] = Field(None, description='', alias='912')
    unsolicitedindicator: Optional[bool] = Field(None, description='', alias='325')
    subscriptionrequesttype: Optional[str] = Field(None, description='', alias='263')
    tradereportrefid: Optional[str] = Field(None, description='', alias='572')
    secondarytradereportrefid: Optional[str] = Field(None, description='', alias='881')
    secondarytradereportid: Optional[str] = Field(None, description='', alias='818')
    tradelinkid: Optional[str] = Field(None, description='', alias='820')
    trdmatchid: Optional[str] = Field(None, description='', alias='880')
    execid: Optional[str] = Field(None, description='', alias='17')
    ordstatus: Optional[str] = Field(None, description='', alias='39')
    secondaryexecid: Optional[str] = Field(None, description='', alias='527')
    execrestatementreason: Optional[int] = Field(None, description='', alias='378')
    previouslyreported: bool = Field(..., description='', alias='570')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    underlyingtradingsessionid: Optional[str] = Field(None, description='', alias='822')
    underlyingtradingsessionsubid: Optional[str] = Field(None, description='', alias='823')
    lastqty: float = Field(..., description='', alias='32')
    lastpx: float = Field(..., description='', alias='31')
    lastparpx: Optional[float] = Field(None, description='', alias='669')
    lastspotrate: Optional[float] = Field(None, description='', alias='194')
    lastforwardpoints: Optional[float] = Field(None, description='', alias='195')
    lastmkt: Optional[str] = Field(None, description='', alias='30')
    tradedate: date = Field(..., description='', alias='75')
    clearingbusinessdate: Optional[date] = Field(None, description='', alias='715')
    avgpx: Optional[float] = Field(None, description='', alias='6')
    avgpxindicator: Optional[int] = Field(None, description='', alias='819')
    multilegreportingtype: Optional[str] = Field(None, description='', alias='442')
    tradelegrefid: Optional[str] = Field(None, description='', alias='824')
    transacttime: datetime = Field(..., description='', alias='60')
    settltype: Optional[str] = Field(None, description='', alias='63')
    settldate: Optional[date] = Field(None, description='', alias='64')
    matchstatus: Optional[str] = Field(None, description='', alias='573')
    matchtype: Optional[str] = Field(None, description='', alias='574')
    copymsgindicator: Optional[bool] = Field(None, description='', alias='797')
    publishtrdindicator: Optional[bool] = Field(None, description='', alias='852')
    shortsalereason: Optional[int] = Field(None, description='', alias='853')
    instrument: Instrument = Field(..., description='Instrument component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    orderqtydata: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    positionamountdata: Optional[PositionAmountData] = Field(None, description='PositionAmountData component')
    trdinstrmtleggrp: Optional[TrdInstrmtLegGrp] = Field(None, description='TrdInstrmtLegGrp component')
    trdregtimestamps: Optional[TrdRegTimestamps] = Field(None, description='TrdRegTimestamps component')
    trdcaprptsidegrp: TrdCapRptSideGrp = Field(..., description='TrdCapRptSideGrp component')

