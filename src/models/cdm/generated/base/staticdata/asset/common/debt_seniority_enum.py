from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DebtSeniorityEnum(CdmModelBase):
    """Specifies the order of repayment in the event of a sale or bankruptcy of the issuer or a related party (eg guarantor)."""
    # Enum values
    Secured: ClassVar[str] = "Secured"
    Senior: ClassVar[str] = "Senior"
    Subordinated: ClassVar[str] = "Subordinated"


# Import after class definition to avoid circular imports
DebtSeniorityEnum.model_rebuild()
