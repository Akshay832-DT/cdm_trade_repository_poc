from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.credit_event_type_enum import CreditEventTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.resource import Resource
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation

class CreditEvent(CdmModelBase):
    """Specifies the relevant data regarding a credit event."""
    credit_event_type: ForwardRef("CreditEventTypeEnum") = Field(description="The type of credit event taking place.")
    event_determination_date: str = Field(description="The date in which the credit event is determined by the Credit Derivatives Determinations Comitee.")
    auction_date: str = Field(None, description="The date on which the auction is scheduled to occur.")
    final_price: ForwardRef("Price") = Field(None, description="The final price resulting from the auction.")
    recovery_percent: float = Field(None, description="The percentage of the original value of the asset affected by the credit event that can be recovered.")
    publicly_available_information: List[ForwardRef("Resource")] = Field(None, description="A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred.")
    reference_information: ForwardRef("ReferenceInformation") = Field(description="The reference entity, part of a credit basket, impacted by the credit event.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.credit_event_type_enum import CreditEventTypeEnum
from src.models.cdm.generated.legaldocumentation.common.resource import Resource
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation
CreditEvent.model_rebuild()
