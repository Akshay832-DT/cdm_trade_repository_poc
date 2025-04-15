from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.limit_applicable_extended import LimitApplicableExtended

class CreditLimitInformation(CdmModelBase):
    """A class to represent the credit limit utilisation information."""
    limit_applicable: List[ForwardRef("LimitApplicableExtended")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.limit_applicable_extended import LimitApplicableExtended
CreditLimitInformation.model_rebuild()
