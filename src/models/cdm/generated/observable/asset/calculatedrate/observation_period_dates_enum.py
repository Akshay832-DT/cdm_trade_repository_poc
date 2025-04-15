from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ObservationPeriodDatesEnum(CdmModelBase):
    """The enumerated values to specify whether rate calculations occur relative to the first or last day of a calculation period. Done in uppercase due to a bug in code generation. This enumeration is used to represent the definitions of modular calculated rates as described in the 2021 ISDA Definitions, section 7."""
    # Enum values
    FixingDate: ClassVar[str] = "FixingDate"
    SetInAdvance: ClassVar[str] = "SetInAdvance"
    Standard: ClassVar[str] = "Standard"


# Import after class definition to avoid circular imports
ObservationPeriodDatesEnum.model_rebuild()
