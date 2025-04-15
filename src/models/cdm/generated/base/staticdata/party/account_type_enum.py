from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AccountTypeEnum(CdmModelBase):
    """The enumeration values to qualify the type of account."""
    # Enum values
    AggregateClient: ClassVar[str] = "AggregateClient"
    Client: ClassVar[str] = "Client"
    House: ClassVar[str] = "House"


# Import after class definition to avoid circular imports
AccountTypeEnum.model_rebuild()
