"""
FIX BasisFeatureDate field (tag 259).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class BasisFeatureDateField(FIXFieldBase):
    """"""
    tag: str = "259"
    name: str = "BasisFeatureDate"
    type: str = "LOCALMKTDATE"
    value: date
