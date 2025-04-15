"""
FIX Component Model - SpreadOrBenchmarkCurveData
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class SpreadOrBenchmarkCurveDataComponent(FIXComponentBase):
    """FIX Component - SpreadOrBenchmarkCurveData"""
    Spread: Optional[float] = Field(None, alias='218', description='')
    BenchmarkCurveCurrency: Optional[str] = Field(None, alias='220', description='')
    BenchmarkCurveName: Optional[str] = Field(None, alias='221', description='')
    BenchmarkCurvePoint: Optional[str] = Field(None, alias='222', description='')
    BenchmarkPrice: Optional[float] = Field(None, alias='662', description='')
    BenchmarkPriceType: Optional[int] = Field(None, alias='663', description='')
    BenchmarkSecurityID: Optional[str] = Field(None, alias='699', description='')
    BenchmarkSecurityIDSource: Optional[str] = Field(None, alias='761', description='')

