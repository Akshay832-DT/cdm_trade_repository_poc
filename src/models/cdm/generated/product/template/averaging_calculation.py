from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.averaging_calculation_method import AveragingCalculationMethod
    from src.models.cdm.generated.base.math.rounding import Rounding

class AveragingCalculation(CdmModelBase):
    """Defines parameters for use in cases when a valuation or other term is based on an average of market observations."""
    averaging_method: ForwardRef("AveragingCalculationMethod") = Field(description="Specifies enumerations for the type of averaging calculation.")
    precision: ForwardRef("Rounding") = Field(description="Rounding applied to the average calculation. ")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.averaging_calculation_method import AveragingCalculationMethod
from src.models.cdm.generated.base.math.rounding import Rounding
AveragingCalculation.model_rebuild()
