from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RateTreatmentEnum(CdmModelBase):
    """The enumerated values to specify the methods for converting rates from one basis to another."""
    # Enum values
    BondEquivalentYield: ClassVar[str] = "BondEquivalentYield"
    MoneyMarketYield: ClassVar[str] = "MoneyMarketYield"


# Import after class definition to avoid circular imports
RateTreatmentEnum.model_rebuild()
