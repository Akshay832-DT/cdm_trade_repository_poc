"""
FIX 4.4 InstrumentExtension Component

This module contains the Pydantic model for the InstrumentExtension component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class InstrumentExtension(FIXMessageBase):
    """
    FIX 4.4 InstrumentExtension Component
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
    deliveryForm: Optional[int] = Field(None, description='', alias='668')
    pctAtRisk: Optional[float] = Field(None, description='', alias='869')
    attrbGrp: Optional[str] = Field(None)
