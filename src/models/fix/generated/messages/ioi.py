"""
FIX 4.4 IOI Message

This module contains the Pydantic model for the IOI message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.ioiqualgrp import IOIQualGrp
from src.models.fix.generated.components.instrmtlegioigrp import InstrmtLegIOIGrp
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.routinggrp import RoutingGrp
from src.models.fix.generated.components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveData
from src.models.fix.generated.components.stipulations import Stipulations
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp
from src.models.fix.generated.components.yielddata import YieldData


class IOI(FIXMessageBase):
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
    
    # Set the message type for this message
    msgType: Literal["6"] = Field("6", alias='35')
    
    # Message-specific fields
    iOIID: Optional[str] = Field(None, description='', alias='23')
    iOITransType: Optional[str] = Field(None, description='', alias='28')
    iOIRefID: Optional[str] = Field(None, description='', alias='26')
    side: Optional[str] = Field(None, description='', alias='54')
    qtyType: Optional[int] = Field(None, description='', alias='854')
    iOIQty: Optional[str] = Field(None, description='', alias='27')
    currency: Optional[str] = Field(None, description='', alias='15')
    priceType: Optional[int] = Field(None, description='', alias='423')
    price: Optional[float] = Field(None, description='', alias='44')
    validUntilTime: Optional[datetime] = Field(None, description='', alias='62')
    iOIQltyInd: Optional[str] = Field(None, description='', alias='25')
    iOINaturalFlag: Optional[bool] = Field(None, description='', alias='130')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    uRLLink: Optional[str] = Field(None, description='', alias='149')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')
    stipulations: Optional[Stipulations] = Field(None, description='Stipulations component')
    instrmtLegIOIGrp: Optional[InstrmtLegIOIGrp] = Field(None, description='InstrmtLegIOIGrp component')
    iOIQualGrp: Optional[IOIQualGrp] = Field(None, description='IOIQualGrp component')
    routingGrp: Optional[RoutingGrp] = Field(None, description='RoutingGrp component')
    spreadOrBenchmarkCurveData: Optional[SpreadOrBenchmarkCurveData] = Field(None, description='SpreadOrBenchmarkCurveData component')
    yieldData: Optional[YieldData] = Field(None, description='YieldData component')

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
