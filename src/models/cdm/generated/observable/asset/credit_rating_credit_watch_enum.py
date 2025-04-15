from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditRatingCreditWatchEnum(CdmModelBase):
    """Represents the enumerated values to specify the credit watch rating."""
    # Enum values
    Developing: ClassVar[str] = "Developing"
    Negative: ClassVar[str] = "Negative"
    Positive: ClassVar[str] = "Positive"


# Import after class definition to avoid circular imports
CreditRatingCreditWatchEnum.model_rebuild()
