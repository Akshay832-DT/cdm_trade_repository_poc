from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CalculationShiftMethodEnum(CdmModelBase):
    """ the specific calculation method, e.g. lookback. This enumeration is used to represent the definitions of modular calculated rates as described in the 2021 ISDA Definitions, section 7."""
    # Enum values
    Lookback: ClassVar[str] = "Lookback"
    NoShift: ClassVar[str] = "NoShift"
    ObservationPeriodShift: ClassVar[str] = "ObservationPeriodShift"
    RateCutOff: ClassVar[str] = "RateCutOff"


# Import after class definition to avoid circular imports
CalculationShiftMethodEnum.model_rebuild()
