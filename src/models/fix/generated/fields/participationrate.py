"""
FIX ParticipationRate field (tag 849).
"""
from .base import FIXFieldBase
from typing import Optional
from .types import *

class ParticipationRateField(FIXFieldBase):
    """"""
    tag: str = "849"
    name: str = "ParticipationRate"
    type: str = "PERCENTAGE"
    value: float
