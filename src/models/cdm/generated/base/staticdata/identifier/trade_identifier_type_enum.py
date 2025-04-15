from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TradeIdentifierTypeEnum(CdmModelBase):
    """Defines the enumerated values to specify the nature of a trade identifier."""
    # Enum values
    UniqueSwapIdentifier: ClassVar[str] = "UniqueSwapIdentifier"
    UniqueTransactionIdentifier: ClassVar[str] = "UniqueTransactionIdentifier"


# Import after class definition to avoid circular imports
TradeIdentifierTypeEnum.model_rebuild()
