from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuantifierEnum(CdmModelBase):
    """Represents the enumerated values to specify a logical quantification, i.e. either All or Any."""
    # Enum values
    All: ClassVar[str] = "All"
    Any: ClassVar[str] = "Any"


# Import after class definition to avoid circular imports
QuantifierEnum.model_rebuild()
