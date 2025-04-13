from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.instrmtlegioigrp import InstrmtLegIOIGrp
from src.models.fix.generated.components.ioiqualgrp import IOIQualGrp
from src.models.fix.generated.components.routinggrp import RoutingGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.yielddata import YieldData

class IOI(FIXMessageBase):
    """FIX message model."""

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    ioiid: str = Field(..., description='', alias='23')
    ioitranstype: str = Field(..., description='', alias='28')
    ioirefid: Optional[str] = Field(None, description='', alias='26')
    side: str = Field(..., description='', alias='54')
    qtytype: Optional[int] = Field(None, description='', alias='854')
    ioiqty: str = Field(..., description='', alias='27')
    currency: Optional[str] = Field(None, description='', alias='15')
    pricetype: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    validuntiltime: Optional[datetime] = Field(None, description='', alias='62')
    ioiqltyind: Optional[str] = Field(None, description='', alias='25')
    ioinaturalflag: Optional[bool] = Field(None, description='', alias='130')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedtextlen: Optional[int] = Field(None, description='', alias='354')
    encodedtext: Optional[str] = Field(None, description='', alias='355')
    transacttime: Optional[datetime] = Field(None, description='', alias='60')
    urllink: Optional[str] = Field(None, description='', alias='149')
    instrument: Instrument = Field(..., description='Instrument component')
    financingdetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undinstrmtgrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderqtydata: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    instrmtlegioigrp: Optional[InstrmtLegIOIGrp] = Field(None, description='InstrmtLegIOIGrp component')
    ioiqualgrp: Optional[IOIQualGrp] = Field(None, description='IOIQualGrp component')
    routinggrp: Optional[RoutingGrp] = Field(None, description='RoutingGrp component')
    spreadorbenchmarkcurvedata: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yielddata: Optional[YieldData] = Field(None, description='YieldData component')

