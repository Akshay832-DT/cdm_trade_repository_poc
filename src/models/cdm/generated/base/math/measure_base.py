from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.unit_type import UnitType

class MeasureBase(CdmModelBase):
    """Provides an abstract type to define a measure as a number associated to a unit. This type is abstract because all its attributes are optional. The types that extend it can specify further existence constraints."""
    value: float = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
    unit: ForwardRef("UnitType") = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.unit_type import UnitType
MeasureBase.model_rebuild()
