from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.fallback_reference_price import FallbackReferencePrice

class PriceSourceDisruption(CdmModelBase):
    """A data defining:  the parameters used to get a price quote to replace the settlement rate option that is disrupted."""
    fallback_reference_price: ForwardRef("FallbackReferencePrice") = Field(description="The method, prioritised by the order it is listed in this element, to get a replacement rate for the disrupted settlement rate option.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.fallback_reference_price import FallbackReferencePrice
PriceSourceDisruption.model_rebuild()
