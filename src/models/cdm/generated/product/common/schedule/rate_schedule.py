from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule

class RateSchedule(CdmModelBase):
    """A class defining a schedule of rates or amounts in terms of an initial value and then a series of step date and value pairs. On each step date the rate or amount changes to the new step value. The series of step date and value pairs are optional. If not specified, this implies that the initial value remains unchanged over time."""
    price: ForwardRef("ReferenceWithMetaPriceSchedule") = Field(description="The initial rate. An initial rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
RateSchedule.model_rebuild()
