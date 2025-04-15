from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AffirmationStatusEnum(CdmModelBase):
    """Enumeration for the different types of affirmation status."""
    # Enum values
    Affirmed: ClassVar[str] = "Affirmed"
    Unaffirmed: ClassVar[str] = "Unaffirmed"


# Import after class definition to avoid circular imports
AffirmationStatusEnum.model_rebuild()
