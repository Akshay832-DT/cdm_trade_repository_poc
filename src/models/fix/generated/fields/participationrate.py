
from .base import FIXFieldBase
from .types import FIXPercentage

class ParticipationRate(FIXFieldBase):
    """FIX ParticipationRate field."""
    tag: str = "849"
    name: str = "ParticipationRate"
    type: str = "PERCENTAGE"
    value: FIXPercentage
