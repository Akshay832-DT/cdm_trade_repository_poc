from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CounterpartyRoleEnum(CdmModelBase):
    """Defines the enumerated values to specify the two counterparties to the transaction."""
    # Enum values
    Party1: ClassVar[str] = "Party1"
    Party2: ClassVar[str] = "Party2"


# Import after class definition to avoid circular imports
CounterpartyRoleEnum.model_rebuild()
