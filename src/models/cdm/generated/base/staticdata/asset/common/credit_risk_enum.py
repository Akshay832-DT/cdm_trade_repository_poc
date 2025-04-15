from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditRiskEnum(CdmModelBase):
    """Represents an enumeration list to identify tranched or untranched credit risk."""
    # Enum values
    TranchedCreditRisk: ClassVar[str] = "TranchedCreditRisk"
    UntranchedCreditRisk: ClassVar[str] = "UntranchedCreditRisk"


# Import after class definition to avoid circular imports
CreditRiskEnum.model_rebuild()
