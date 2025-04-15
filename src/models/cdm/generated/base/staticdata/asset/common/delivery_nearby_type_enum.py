from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DeliveryNearbyTypeEnum(CdmModelBase):
    """"""
    # Enum values
    CalculationPeriod: ClassVar[str] = "CalculationPeriod"
    NearbyMonth: ClassVar[str] = "NearbyMonth"
    NearbyWeek: ClassVar[str] = "NearbyWeek"


# Import after class definition to avoid circular imports
DeliveryNearbyTypeEnum.model_rebuild()
