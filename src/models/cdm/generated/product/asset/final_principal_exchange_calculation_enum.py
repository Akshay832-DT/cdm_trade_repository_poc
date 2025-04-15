from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FinalPrincipalExchangeCalculationEnum(CdmModelBase):
    """To be specified only for products that embed a redemption payment."""
    # Enum values
    Floored: ClassVar[str] = "Floored"
    NonFloored: ClassVar[str] = "NonFloored"


# Import after class definition to avoid circular imports
FinalPrincipalExchangeCalculationEnum.model_rebuild()
