"""
FIX 4.4 ContraGrp Component

This module contains the Pydantic model for the ContraGrp component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class NoContraBrokersGroup(FIXComponentBase):
    """
    NoContraBrokers group fields
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
    
    ContraBroker: Optional[str] = Field(None, description='', alias='375')
    ContraTrader: Optional[str] = Field(None, description='', alias='337')
    ContraTradeQty: Optional[float] = Field(None, description='', alias='437')
    ContraTradeTime: Optional[datetime] = Field(None, description='', alias='438')
    ContraLegRefID: Optional[str] = Field(None, description='', alias='655')


class ContraGrpComponent(FIXComponentBase):
    """
    FIX 4.4 ContraGrp Component
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
    
    NoContraBrokers: Optional[int] = Field(None, description='Number of NoContraBrokers entries', alias='')
    NoContraBrokers_items: List[NoContraBrokersGroup] = Field(default_factory=list)
