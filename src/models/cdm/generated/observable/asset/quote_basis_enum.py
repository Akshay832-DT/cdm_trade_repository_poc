from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuoteBasisEnum(CdmModelBase):
    """The enumerated values to specify how an exchange rate is quoted."""
    # Enum values
    Currency1PerCurrency2: ClassVar[str] = "Currency1PerCurrency2"
    Currency2PerCurrency1: ClassVar[str] = "Currency2PerCurrency1"


# Import after class definition to avoid circular imports
QuoteBasisEnum.model_rebuild()
