from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditRatingOutlookEnum(CdmModelBase):
    """Represents the enumerated values to specify the credit rating outlook."""
    # Enum values
    Developing: ClassVar[str] = "Developing"
    Negative: ClassVar[str] = "Negative"
    Positive: ClassVar[str] = "Positive"
    Stable: ClassVar[str] = "Stable"


# Import after class definition to avoid circular imports
CreditRatingOutlookEnum.model_rebuild()
