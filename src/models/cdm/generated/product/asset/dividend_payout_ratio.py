from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_basket_constituent import ReferenceWithMetaBasketConstituent

class DividendPayoutRatio(CdmModelBase):
    """A class describing the dividend payout ratio associated with an equity underlier. In certain cases the actual ratio is not known on trade inception, and only general conditions are then specified."""
    total_ratio: float = Field(description="Specifies the total actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
    cash_ratio: float = Field(None, description="Specifies the cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
    non_cash_ratio: float = Field(None, description="Specifies the non cash actual dividend payout ratio associated with the equity underlier. A ratio of 90% should be expressed at 0.90.")
    basket_constituent: ForwardRef("ReferenceWithMetaBasketConstituent") = Field(None, description="In the case of a basket underlier, specifies to which component of the basket this particular set of dividend payout ratios correspond.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_basket_constituent import ReferenceWithMetaBasketConstituent
DividendPayoutRatio.model_rebuild()
