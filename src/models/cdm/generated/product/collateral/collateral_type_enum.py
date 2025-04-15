from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CollateralTypeEnum(CdmModelBase):
    """Specifies the types of collateral that are accepted by the Lender"""
    # Enum values
    Cash: ClassVar[str] = "Cash"
    CashPool: ClassVar[str] = "CashPool"
    NonCash: ClassVar[str] = "NonCash"


# Import after class definition to avoid circular imports
CollateralTypeEnum.model_rebuild()
