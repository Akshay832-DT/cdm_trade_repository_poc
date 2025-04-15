from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.averaging_schedule import AveragingSchedule
    from src.models.cdm.generated.base.datetime.date_list import DateList
    from src.models.cdm.generated.observable.event.feature_payment import FeaturePayment
    from src.models.cdm.generated.observable.event.trigger import Trigger

class TriggerEvent(CdmModelBase):
    """Observation point for trigger."""
    schedule: List[ForwardRef("AveragingSchedule")] = Field(None, description="A derivative schedule.")
    trigger_dates: ForwardRef("DateList") = Field(None, description="The trigger Dates.")
    trigger: ForwardRef("Trigger") = Field(description="The trigger level")
    feature_payment: ForwardRef("FeaturePayment") = Field(None, description="The feature payment, i.e. the payment made following trigger occurrence.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.averaging_schedule import AveragingSchedule
from src.models.cdm.generated.base.datetime.date_list import DateList
from src.models.cdm.generated.observable.event.feature_payment import FeaturePayment
from src.models.cdm.generated.observable.event.trigger import Trigger
TriggerEvent.model_rebuild()
