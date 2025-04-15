from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_fixed_rate_specification import ReferenceWithMetaFixedRateSpecification
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.observable.asset.reference_swap_curve import ReferenceSwapCurve
    from src.models.cdm.generated.product.template.averaging_strike_feature import AveragingStrikeFeature

class OptionStrike(CdmModelBase):
    """Defines the strike price of an option."""
    strike_price: ForwardRef("Price") = Field(None, description="Defines the strike of an option in the form of a price that could be a cash price, interestRate, or other types.")
    strike_reference: ForwardRef("ReferenceWithMetaFixedRateSpecification") = Field(None, description="Defines the strike of an option in reference to the spread of the underlying swap (typical practice in the case of an option on a credit single name swaps).")
    reference_swap_curve: ForwardRef("ReferenceSwapCurve") = Field(None, description="Defines the strike of an option when expressed by reference to a swap curve (Typically the case for a convertible bond option).")
    averaging_strike_feature: ForwardRef("AveragingStrikeFeature") = Field(None, description="Defines an  option strike that is calculated from an average of observed market prices.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_fixed_rate_specification import ReferenceWithMetaFixedRateSpecification
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.observable.asset.reference_swap_curve import ReferenceSwapCurve
from src.models.cdm.generated.product.template.averaging_strike_feature import AveragingStrikeFeature
OptionStrike.model_rebuild()
