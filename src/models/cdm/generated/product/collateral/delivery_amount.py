from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.delivery_amount_election_enum import DeliveryAmountElectionEnum

class DeliveryAmount(CdmModelBase):
    """A class to specify the application of Interest Amount with respect the Delivery Amount."""
    standard_election: ForwardRef("DeliveryAmountElectionEnum") = Field(None, description="The standard election as specified by an enumeration.")
    custom_election: str = Field(None, description="The custom election that might be specified by the parties to the agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.delivery_amount_election_enum import DeliveryAmountElectionEnum
DeliveryAmount.model_rebuild()
