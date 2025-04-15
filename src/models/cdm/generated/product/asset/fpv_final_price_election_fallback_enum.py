from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FPVFinalPriceElectionFallbackEnum(CdmModelBase):
    """Specifies the fallback provisions in respect to the applicable Futures Price Valuation."""
    # Enum values
    FPVClose: ClassVar[str] = "FPVClose"
    FPVHedgeExecution: ClassVar[str] = "FPVHedgeExecution"


# Import after class definition to avoid circular imports
FPVFinalPriceElectionFallbackEnum.model_rebuild()
