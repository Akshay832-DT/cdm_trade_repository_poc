"""FIX message model for IOI (6).

Category: 
"""
from typing import List, Optional
from datetime import date, datetime, time
from pydantic import Field
from ..base import FIXMessageBase
from ..components.financingdetails import FinancingDetailsComponent
from ..components.ioiqualgrp import IOIQualGrpComponent
from ..components.instrmtlegioigrp import InstrmtLegIOIGrpComponent
from ..components.instrument import InstrumentComponent
from ..components.orderqtydata import OrderQtyDataComponent
from ..components.routinggrp import RoutingGrpComponent
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
from ..components.stipulations import StipulationsComponent
from ..components.undinstrmtgrp import UndInstrmtGrpComponent
from ..components.yielddata import YieldDataComponent

class IOIMessage(FIXMessageBase):
    """FIX message model for IOI."""

    MsgType: str = Field("6", alias="35")

    IOIID: str = Field(..., alias='23', description='')
    IOITransType: str = Field(..., alias='28', description='')
    IOIRefID: Optional[str] = Field(None, alias='26', description='')
    Side: str = Field(..., alias='54', description='')
    QtyType: Optional[int] = Field(None, alias='854', description='')
    IOIQty: str = Field(..., alias='27', description='')
    Currency: Optional[str] = Field(None, alias='15', description='')
    PriceType: Optional[int] = Field(None, alias='423', description='')
    Price: Optional[float] = Field(None, alias='44', description='')
    ValidUntilTime: Optional[datetime] = Field(None, alias='62', description='')
    IOIQltyInd: Optional[str] = Field(None, alias='25', description='')
    IOINaturalFlag: Optional[bool] = Field(None, alias='130', description='')
    Text: Optional[str] = Field(None, alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')
    TransactTime: Optional[datetime] = Field(None, alias='60', description='')
    URLLink: Optional[str] = Field(None, alias='149', description='')
    Instrument: InstrumentComponent = Field(..., description='')
    FinancingDetails: Optional[FinancingDetailsComponent] = Field(None, description='')
    UndInstrmtGrp: Optional[UndInstrmtGrpComponent] = Field(None, description='')
    OrderQtyData: Optional[OrderQtyDataComponent] = Field(None, description='')
    Stipulations: Optional[StipulationsComponent] = Field(None, description='')
    InstrmtLegIOIGrp: Optional[InstrmtLegIOIGrpComponent] = Field(None, description='')
    IOIQualGrp: Optional[IOIQualGrpComponent] = Field(None, description='')
    RoutingGrp: Optional[RoutingGrpComponent] = Field(None, description='')
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveDataComponent] = Field(None, description='')
    YieldData: Optional[YieldDataComponent] = Field(None, description='')

