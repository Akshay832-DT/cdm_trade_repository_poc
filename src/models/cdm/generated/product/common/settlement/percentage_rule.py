from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney

class PercentageRule(CdmModelBase):
    """A class defining a content model for a calculation rule defined as percentage of the notional amount."""
    payment_percent: float = Field(description="A percentage of the notional amount.")
    notional_amount_reference: ForwardRef("ReferenceWithMetaMoney") = Field(description="A reference to the notional amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney
PercentageRule.model_rebuild()
