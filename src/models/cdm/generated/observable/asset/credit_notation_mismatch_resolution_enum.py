from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditNotationMismatchResolutionEnum(CdmModelBase):
    """Represents an enumeration list to identify the characteristics of the rating if there are several agency issue ratings but not equivalent, reference will be made to label characteristics of the rating such as the lowest/highest available."""
    # Enum values
    Average: ClassVar[str] = "Average"
    Highest: ClassVar[str] = "Highest"
    Lowest: ClassVar[str] = "Lowest"
    Other: ClassVar[str] = "Other"
    ReferenceAgency: ClassVar[str] = "ReferenceAgency"
    SecondBest: ClassVar[str] = "SecondBest"


# Import after class definition to avoid circular imports
CreditNotationMismatchResolutionEnum.model_rebuild()
