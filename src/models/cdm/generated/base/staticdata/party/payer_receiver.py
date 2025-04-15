from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum

class PayerReceiver(CdmModelBase):
    """Specifies the parties responsible for making and receiving payments defined by this structure."""
    payer: ForwardRef("CounterpartyRoleEnum") = Field(description="Specifies the counterparty responsible for making the payments defined by this structure.  The party is one of the two principal parties to the transaction.")
    receiver: ForwardRef("CounterpartyRoleEnum") = Field(description="Specifies the party that receives the payments corresponding to this structure.  The party is one of the two counterparties to the transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
PayerReceiver.model_rebuild()
