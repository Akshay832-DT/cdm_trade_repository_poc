from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver_enum import PayerReceiverEnum
    from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule

class StrikeSchedule(CdmModelBase):
    """A class describing a schedule of cap or floor rates."""
    price: ForwardRef("ReferenceWithMetaPriceSchedule") = Field(None, description="The initial rate. An initial rate of 5% would be represented as 0.05.")
    buyer: ForwardRef("PayerReceiverEnum") = Field(None, description="The buyer of the option.")
    seller: ForwardRef("PayerReceiverEnum") = Field(None, description="The party that has sold.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver_enum import PayerReceiverEnum
from src.models.cdm.generated.metafields.reference_with_meta_price_schedule import ReferenceWithMetaPriceSchedule
StrikeSchedule.model_rebuild()
