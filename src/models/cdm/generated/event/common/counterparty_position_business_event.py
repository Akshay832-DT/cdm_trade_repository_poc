from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
    from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
    from src.models.cdm.generated.event.common.counterparty_position_state import CounterpartyPositionState
    from src.models.cdm.generated.event.common.position_event_intent_enum import PositionEventIntentEnum

class CounterpartyPositionBusinessEvent(CdmModelBase):
    """A business event represents a life cycle event of a position. The combination of the state changes results in a qualifiable life cycle event."""
    intent: ForwardRef("PositionEventIntentEnum") = Field(description="The intent attribute is meant to be specified when the event qualification cannot be programmatically inferred from the event features. As a result it is only associated with those primitives that can give way to such ambiguity, the quantityChange being one of those.")
    corporate_action_intent: ForwardRef("CorporateActionTypeEnum") = Field(None, description="The intent of a corporate action on the position.")
    event_date: str = Field(None, description="Specifies the date on which the event is taking place. This date is equal to the trade date in the case of a simple execution.  However it can be different from the trade date, for example in the case of a partial termination.")
    effective_date: str = Field(None, description="The date on which the event contractually takes effect, when different from the event date.")
    package_information: ForwardRef("IdentifiedList") = Field(None, description="Specifies the package information in case the business event represents several trades executed as a package (hence this attribute is optional). The package information is only instantiated once at the business event level to preserve referential integrity, whereas individual trades make reference to it to identify that they are part of a package.")
    after: List[ForwardRef("CounterpartyPositionState")] = Field(None, description="Specifies the after position state(s) created.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
from src.models.cdm.generated.event.common.counterparty_position_state import CounterpartyPositionState
from src.models.cdm.generated.event.common.position_event_intent_enum import PositionEventIntentEnum
CounterpartyPositionBusinessEvent.model_rebuild()
