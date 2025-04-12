"""
FIX 4.4 SpreadOrBenchmarkCurveData Component

This module contains the Pydantic model for the SpreadOrBenchmarkCurveData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXMessageBase


class SpreadOrBenchmarkCurveData(FIXMessageBase):
    """
    FIX 4.4 SpreadOrBenchmarkCurveData Component
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
    spread: Optional[float] = Field(None, description='', alias='218')
    benchmarkCurveCurrency: Optional[str] = Field(None, description='', alias='220')
    benchmarkCurveName: Optional[str] = Field(None, description='', alias='221')
    benchmarkCurvePoint: Optional[str] = Field(None, description='', alias='222')
    benchmarkPrice: Optional[float] = Field(None, description='', alias='662')
    benchmarkPriceType: Optional[int] = Field(None, description='', alias='663')
    benchmarkSecurityID: Optional[str] = Field(None, description='', alias='699')
    benchmarkSecurityIDSource: Optional[str] = Field(None, description='', alias='761')
