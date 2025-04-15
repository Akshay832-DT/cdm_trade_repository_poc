from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
    from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
    from src.models.cdm.generated.event.common.event_intent_enum import EventIntentEnum
    from src.models.cdm.generated.event.common.instruction import Instruction

class EventInstruction(CdmModelBase):
    """Specifies instructions to create a BusinessEvent."""
    intent: ForwardRef("EventIntentEnum") = Field(None, description="The intent attribute is meant to be specified when the event qualification cannot be programmatically inferred from the event features. As a result it is only associated with those primitives that can give way to such ambiguity, the quantityChange being one of those. An example of such is a reduction in the trade notional, which could be interpreted as either a trade correction (unless a maximum period of time post-event is specified as part of the qualification), a partial termination or a portfolio rebalancing in the case of an equity swap. On the other hand, an event such as the exercise is not expected to have an associated intent as there should not be ambiguity.")
    corporate_action_intent: ForwardRef("CorporateActionTypeEnum") = Field(None)
    event_date: str = Field(None, description="Specifies the date on which the event is taking place. This date is equal to the trade date in the case of a simple execution.  However it can be different from the trade date, for example in the case of a partial termination.")
    effective_date: str = Field(None, description="The date on which the event contractually takes effect, when different from the event date.")
    package_information: ForwardRef("IdentifiedList") = Field(None, description="Specifies the package information in case the business event represents several trades executed as a package (hence this attribute is optional). The package information is only instantiated once at the business event level to preserve referential integrity, whereas individual trades make reference to it to identify that they are part of a package.")
    instruction: List[ForwardRef("Instruction")] = Field(None, description="Specifies the instructions to create the Business Event.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identified_list import IdentifiedList
from src.models.cdm.generated.event.common.corporate_action_type_enum import CorporateActionTypeEnum
from src.models.cdm.generated.event.common.event_intent_enum import EventIntentEnum
from src.models.cdm.generated.event.common.instruction import Instruction
EventInstruction.model_rebuild()
