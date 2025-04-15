from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.averaging_calculation_method_enum import AveragingCalculationMethodEnum

class AveragingCalculationMethod(CdmModelBase):
    """Defines the ways in which multiple values can be aggregated into a single value."""
    is_weighted: bool = Field(description="Identifies whether the average values will be weighted or unweighted.")
    calculation_method: ForwardRef("AveragingCalculationMethodEnum") = Field(description="Identifies which of the Pythagorean means is being used to compute an average value.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.averaging_calculation_method_enum import AveragingCalculationMethodEnum
AveragingCalculationMethod.model_rebuild()
