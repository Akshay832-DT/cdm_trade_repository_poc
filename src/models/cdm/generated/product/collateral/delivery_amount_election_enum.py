from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DeliveryAmountElectionEnum(CdmModelBase):
    """The enumerated values to specify the application of Interest Amount with respect to the Delivery Amount through standard language."""
    # Enum values
    LastAndAnyLocalBusinessDay: ClassVar[str] = "LastAndAnyLocalBusinessDay"
    LastLocalBusinessDay: ClassVar[str] = "LastLocalBusinessDay"


# Import after class definition to avoid circular imports
DeliveryAmountElectionEnum.model_rebuild()
