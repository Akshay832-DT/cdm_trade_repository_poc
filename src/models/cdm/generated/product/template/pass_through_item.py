from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver

class PassThroughItem(CdmModelBase):
    """Class to represent a single pass through payment."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(description="This attribute doesn't exists in the FpML construct, which makes use of the PayerReceiver.model group.")
    pass_through_percentage: float = Field(description="Percentage of payments from the underlier which are passed through.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
PassThroughItem.model_rebuild()
