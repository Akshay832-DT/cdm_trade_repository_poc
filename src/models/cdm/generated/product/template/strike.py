from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver_enum import PayerReceiverEnum

class Strike(CdmModelBase):
    """A class describing a single cap or floor rate."""
    strike_rate: float = Field(description="The rate for a cap or floor.")
    buyer: ForwardRef("PayerReceiverEnum") = Field(None, description="The buyer of the option.")
    seller: ForwardRef("PayerReceiverEnum") = Field(None, description="The party that has sold.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver_enum import PayerReceiverEnum
Strike.model_rebuild()
