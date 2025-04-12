"""
FIX 4.4 IOI Message

This module contains the Pydantic model for the IOI message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.financingdetails import FinancingDetails
from ..components.ioiqualgrp import IOIQualGrp
from ..components.instrmtlegioigrp import InstrmtLegIOIGrp
from ..components.instrument import Instrument
from ..components.orderqtydata import OrderQtyData
from ..components.routinggrp import RoutingGrp
from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from ..components.stipulations import Stipulations
from ..components.undinstrmtgrp import UndInstrmtGrp
from ..components.yielddata import YieldData


class IOI(TradeModel):
    """
    FIX 4.4 IOI Message
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
    MsgType: Literal["6"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    IOIID: str = Field(None, description='', alias='23')
    IOITransType: str = Field(None, description='', alias='28')
    IOIRefID: Optional[str] = Field(None, description='', alias='26')
    Side: str = Field(None, description='', alias='54')
    QtyType: Optional[int] = Field(None, description='', alias='854')
    IOIQty: str = Field(None, description='', alias='27')
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
    Instrument: Instrument = Field(..., description='Instrument component')
    FinancingDetails: Optional[FinancingDetails] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    OrderQtyData: Optional[OrderQtyData] = None
    Stipulations: Optional[Stipulations] = None
    InstrmtLegIOIGrp: Optional[InstrmtLegIOIGrp] = None
    IOIQualGrp: Optional[IOIQualGrp] = None
    RoutingGrp: Optional[RoutingGrp] = None
    SpreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = None
    YieldData: Optional[YieldData] = None

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
