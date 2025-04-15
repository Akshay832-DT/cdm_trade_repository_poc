from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_credit_events import ReferenceWithMetaCreditEvents
    from src.models.cdm.generated.observable.asset.price_schedule import PriceSchedule
    from src.models.cdm.generated.observable.event.credit_events import CreditEvents
    from src.models.cdm.generated.observable.event.trigger_time_type_enum import TriggerTimeTypeEnum
    from src.models.cdm.generated.observable.event.trigger_type_enum import TriggerTypeEnum

class Trigger(CdmModelBase):
    """Trigger point at which feature is effective."""
    level: List[ForwardRef("PriceSchedule")] = Field(None, description="The trigger level.")
    credit_events: ForwardRef("CreditEvents") = Field(None)
    credit_events_reference: ForwardRef("ReferenceWithMetaCreditEvents") = Field(None)
    trigger_type: ForwardRef("TriggerTypeEnum") = Field(None, description="The Triggering condition.")
    trigger_time_type: ForwardRef("TriggerTimeTypeEnum") = Field(None, description="The valuation time type of knock condition.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_credit_events import ReferenceWithMetaCreditEvents
from src.models.cdm.generated.observable.asset.price_schedule import PriceSchedule
from src.models.cdm.generated.observable.event.credit_events import CreditEvents
from src.models.cdm.generated.observable.event.trigger_time_type_enum import TriggerTimeTypeEnum
from src.models.cdm.generated.observable.event.trigger_type_enum import TriggerTypeEnum
Trigger.model_rebuild()
