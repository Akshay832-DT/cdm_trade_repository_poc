from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.corporate_action import CorporateAction
    from src.models.cdm.generated.event.common.credit_event import CreditEvent

class ObservationEvent(CdmModelBase):
    """Specifies the necessary information to create any observation event."""
    credit_event: ForwardRef("CreditEvent") = Field(None, description="Specifies the necessary information to create a credit event.")
    corporate_action: ForwardRef("CorporateAction") = Field(None, description="Specifies the necessary information to create a corporate action.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.corporate_action import CorporateAction
from src.models.cdm.generated.event.common.credit_event import CreditEvent
ObservationEvent.model_rebuild()
