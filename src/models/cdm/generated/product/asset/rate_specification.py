from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.fixed_rate_specification import FixedRateSpecification
    from src.models.cdm.generated.product.asset.floating_rate_specification import FloatingRateSpecification
    from src.models.cdm.generated.product.asset.inflation_rate_specification import InflationRateSpecification

class RateSpecification(CdmModelBase):
    """ A data type to specify the fixed interest rate, floating interest rate or inflation rate."""
    fixed_rate_specification: ForwardRef("FixedRateSpecification") = Field(None, description="The fixed rate or fixed rate specification expressed as explicit fixed rates and dates.")
    floating_rate_specification: ForwardRef("FloatingRateSpecification") = Field(None, description="The floating interest rate specification, which includes the definition of the floating rate index. the tenor, the initial value, and, when applicable, the spread, the rounding convention, the averaging method and the negative interest rate treatment.")
    inflation_rate_specification: ForwardRef("InflationRateSpecification") = Field(None, description="An inflation rate calculation definition.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.fixed_rate_specification import FixedRateSpecification
from src.models.cdm.generated.product.asset.floating_rate_specification import FloatingRateSpecification
from src.models.cdm.generated.product.asset.inflation_rate_specification import InflationRateSpecification
RateSpecification.model_rebuild()
