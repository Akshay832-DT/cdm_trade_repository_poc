from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.money_range import MoneyRange
    from src.models.cdm.generated.base.math.number_range import NumberRange
    from src.models.cdm.generated.product.collateral.concentration_limit_criteria import ConcentrationLimitCriteria

class ConcentrationLimit(CdmModelBase):
    """Represents a class to describe concentration limits that may be applicable to eligible collateral criteria."""
    concentration_limit_criteria: ForwardRef("ConcentrationLimitCriteria") = Field(None, description="Specifies a set of criteria to describe the assets that the concentration limits apply to.")
    value_limit: ForwardRef("MoneyRange") = Field(None, description="Specifies the value of collateral limit represented as a range.")
    percentage_limit: ForwardRef("NumberRange") = Field(None, description="Specifies the perecentage of collateral limit represented as a decimal number - example 25% is 0.25.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.money_range import MoneyRange
from src.models.cdm.generated.base.math.number_range import NumberRange
from src.models.cdm.generated.product.collateral.concentration_limit_criteria import ConcentrationLimitCriteria
ConcentrationLimit.model_rebuild()
