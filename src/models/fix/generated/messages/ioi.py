from typing import Optional, List
from datetime import datetime, date, time
from pydantic import Field
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.components.instrument import InstrumentComponent
from src.models.fix.generated.components.financingdetails import FinancingDetailsComponent
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrpComponent
from src.models.fix.generated.components.orderqtydata import OrderQtyDataComponent
from src.models.fix.generated.components.stipulations import StipulationsComponent
from src.models.fix.generated.components.instrmtlegioigrp import InstrmtLegIOIGrpComponent
from src.models.fix.generated.components.ioiqualgrp import IOIQualGrpComponent
from src.models.fix.generated.components.routinggrp import RoutingGrpComponent
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from src.models.fix.generated.components.yielddata import YieldDataComponent

class IOI(FIXMessageBase):
    """FIX message model."""

    BeginString: str = Field(..., description='', alias='8')
    BodyLength: int = Field(..., description='', alias='9')
    MsgType: str = Field(..., description='', alias='35')
    SenderCompID: str = Field(..., description='', alias='49')
    TargetCompID: str = Field(..., description='', alias='56')
    MsgSeqNum: int = Field(..., description='', alias='34')
    SendingTime: datetime = Field(..., description='', alias='52')
    IOIID: str = Field(..., description='', alias='23')
    IOITransType: str = Field(..., description='', alias='28')
    IOIRefID: Optional[str] = Field(None, description='', alias='26')
    Side: str = Field(..., description='', alias='54')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    IOIQty: str = Field(..., description='', alias='27')
    Currency: Optional[str] = Field(None, description='', alias='15')
    PriceType: Optional[int] = Field(None, description='', alias='423')
    Price: Optional[float] = Field(None, description='', alias='44')
    ValidUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    IOIQltyInd: Optional[str] = Field(None, description='', alias='25')
    IOINaturalFlag: Optional[bool] = Field(None, description='', alias='130')
    Text: Optional[str] = Field(None, description='', alias='58')
    EncodedTextLen: Optional[int] = Field(None, description='', alias='354')
    EncodedText: Optional[str] = Field(None, description='', alias='355')
    TransactTime: Optional[datetime] = Field(None, description='', alias='60')
    URLLink: Optional[str] = Field(None, description='', alias='149')
    Instrument: InstrumentComponent = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='FinancingDetails component')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='UndInstrmtGrp component')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='OrderQtyData component')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='Stipulations component')
    InstrmtLegIOIGrp: Optional[InstrmtLegIOIGrpComponent] = Field(None, description='InstrmtLegIOIGrp component')
    IOIQualGrp: Optional[IOIQualGrpComponent] = Field(None, description='IOIQualGrp component')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='RoutingGrp component')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='SpreadOrBenchmarkCurveData component')
    YieldData: Optional[YieldDataComponent] = Field(None, description='YieldData component')

