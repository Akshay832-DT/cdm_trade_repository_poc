"""
FIX 4.4 SpreadOrBenchmarkCurveData Component

This module contains the Pydantic model for the SpreadOrBenchmarkCurveData component.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import Field, ConfigDict
from src.models.fix.generated.fields.common import *
from src.models.fix.base import FIXComponentBase
class SpreadOrBenchmarkCurveDataComponent(FIXComponentBase):
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
    
    Spread: Optional[float] = Field(None, description='', alias='218')
    BenchmarkCurveCurrency: Optional[str] = Field(None, description='', alias='220')
    BenchmarkCurveName: Optional[str] = Field(None, description='', alias='221')
    BenchmarkCurvePoint: Optional[str] = Field(None, description='', alias='222')
    BenchmarkPrice: Optional[float] = Field(None, description='', alias='662')
    BenchmarkPriceType: Optional[int] = Field(None, description='', alias='663')
    BenchmarkSecurityID: Optional[str] = Field(None, description='', alias='699')
    BenchmarkSecurityIDSource: Optional[str] = Field(None, description='', alias='761')
