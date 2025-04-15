from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.closed_state_enum import ClosedStateEnum

class ClosedState(CdmModelBase):
    """ A class to qualify the closed state of an execution or a contract through the combination or a state (e.g. terminated, novated) and a set of dates: activity date, effective date and, when relevant, last payment date."""
    state: ForwardRef("ClosedStateEnum") = Field(description="The qualification of what gave way to the contract or execution closure, e.g. allocation, termination, ...")
    activity_date: str = Field(description="The activity date on which the closing state took place, i.e. either the event date of the closing event (e.g. option exercise, contract early termination) or the contractual termination date.")
    effective_date: str = Field(None, description="The date on which the closing event contractually takes effect, when different from the activity date. When an explicit event effective date attribute is associated with the closing event, it will be that date. In the case of a cancellation event, it will be the date on which the cancelled event took place.")
    last_payment_date: str = Field(None, description="The date associated with the last payment in relation to the artefact (e.g. contract) to which this closed state applies. As an example, in the case of an early termination event, it would be the settlement date of the associated fee, if applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.closed_state_enum import ClosedStateEnum
ClosedState.model_rebuild()
