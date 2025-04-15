from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.realised_variance_method_enum import RealisedVarianceMethodEnum

class BoundedVariance(CdmModelBase):
    """"""
    realised_variance_method: ForwardRef("RealisedVarianceMethodEnum") = Field(description="The contract specifies which price must satisfy the boundary condition.")
    days_in_range_adjustment: bool = Field(description="The contract specifies whether the notional should be scaled by the Number of Days in Range divided by the Expected N. The number of Days in Ranges refers to the number of returns that contribute to the realized volatility.")
    upper_barrier: float = Field(None, description="All observations above this price level will be excluded from the variance calculation.")
    lower_barrier: float = Field(None, description="All observations below this price level will be excluded from the variance calculation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.realised_variance_method_enum import RealisedVarianceMethodEnum
BoundedVariance.model_rebuild()
