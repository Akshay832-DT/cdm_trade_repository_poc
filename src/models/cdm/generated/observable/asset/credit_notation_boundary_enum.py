from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditNotationBoundaryEnum(CdmModelBase):
    """Identifies an agency rating as a simple scale boundary of minimum or maximum."""
    # Enum values
    Maximum: ClassVar[str] = "Maximum"
    Minimum: ClassVar[str] = "Minimum"


# Import after class definition to avoid circular imports
CreditNotationBoundaryEnum.model_rebuild()
