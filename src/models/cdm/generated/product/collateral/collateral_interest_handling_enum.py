from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CollateralInterestHandlingEnum(CdmModelBase):
    """How is collateral interest to be handled?"""
    # Enum values
    Adjust: ClassVar[str] = "Adjust"
    Transfer: ClassVar[str] = "Transfer"
    Transfer_or_Adjust: ClassVar[str] = "Transfer_or_Adjust"


# Import after class definition to avoid circular imports
CollateralInterestHandlingEnum.model_rebuild()
