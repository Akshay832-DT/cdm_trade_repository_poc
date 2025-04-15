"""
FIX Component Model - LegBenchmarkCurveData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class LegBenchmarkCurveDataComponent(FIXComponentBase):
    """FIX Component - LegBenchmarkCurveData"""
    LegBenchmarkCurveCurrency: Optional[str] = Field(None, alias='676', description='')
    LegBenchmarkCurveName: Optional[str] = Field(None, alias='677', description='')
    LegBenchmarkCurvePoint: Optional[str] = Field(None, alias='678', description='')
    LegBenchmarkPrice: Optional[float] = Field(None, alias='679', description='')
    LegBenchmarkPriceType: Optional[int] = Field(None, alias='680', description='')

