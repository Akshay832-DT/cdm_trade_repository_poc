from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.observable.asset.premium_type_enum import PremiumTypeEnum

class PremiumExpression(CdmModelBase):
    """This class corresponds to the FpML Premium.model group for representing the option premium when expressed in a way other than an amount."""
    premium_type: ForwardRef("PremiumTypeEnum") = Field(None, description="Forward start premium type")
    price_per_option: ForwardRef("Money") = Field(None, description="The amount of premium to be paid expressed as a function of the number of options.")
    percentage_of_notional: float = Field(None, description="The amount of premium to be paid expressed as a percentage of the notional value of the transaction. A percentage of 5% would be expressed as 0.05.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.observable.asset.premium_type_enum import PremiumTypeEnum
PremiumExpression.model_rebuild()
