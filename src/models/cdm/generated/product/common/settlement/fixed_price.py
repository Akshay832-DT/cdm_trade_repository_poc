from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule

class FixedPrice(CdmModelBase):
    """A predefined price accorded by the counterparties."""
    price: ForwardRef("ReferenceWithMetaPriceSchedule") = Field(None, description="Fixed price step schedule, including an initial price specified as an absolute number.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
FixedPrice.model_rebuild()
