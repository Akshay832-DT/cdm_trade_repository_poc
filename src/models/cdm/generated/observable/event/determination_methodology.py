from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.averaging_calculation_method_enum import AveragingCalculationMethodEnum
    from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum

class DeterminationMethodology(CdmModelBase):
    """Specifies the method according to which an amount or a date is determined."""
    determination_method: ForwardRef("DeterminationMethodEnum") = Field(None, description="Represents a more granular dimention of observation. Typically relevent for resolving a unique equity price, which can be expressed as trade-weighted or volume-weighted averages.")
    averaging_method: ForwardRef("AveragingCalculationMethodEnum") = Field(None, description="Specifies enumerations for the type of averaging calculation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.averaging_calculation_method_enum import AveragingCalculationMethodEnum
from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
DeterminationMethodology.model_rebuild()
