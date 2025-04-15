from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_spread_schedule_type_enum import FieldWithMetaSpreadScheduleTypeEnum
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule

class SpreadSchedule(CdmModelBase):
    """Adds an optional spread type element to the Schedule to identify a long or short spread value."""
    price: ForwardRef("ReferenceWithMetaPriceSchedule") = Field(None, description="The initial rate. An initial rate of 5% would be represented as 0.05.")
    spread_schedule_type: ForwardRef("FieldWithMetaSpreadScheduleTypeEnum") = Field(None, description="An element which purpose is to identify a long or short spread value.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_spread_schedule_type_enum import FieldWithMetaSpreadScheduleTypeEnum
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
SpreadSchedule.model_rebuild()
