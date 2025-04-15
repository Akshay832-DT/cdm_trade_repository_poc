from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DiscountingTypeEnum(CdmModelBase):
    """The enumerated values to specify the method of calculating discounted payment amounts. This enumerations combines the FpML DiscountingTypeEnum and FraDiscountingEnum enumerations."""
    # Enum values
    AFMA: ClassVar[str] = "AFMA"
    FRA: ClassVar[str] = "FRA"
    FRAYield: ClassVar[str] = "FRAYield"
    Standard: ClassVar[str] = "Standard"


# Import after class definition to avoid circular imports
DiscountingTypeEnum.model_rebuild()
