from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SpecifiedEntityClauseEnum(CdmModelBase):
    """The enumerated values to specify the Event of Default or Termination event for which Specified Entities terms are being defined."""
    # Enum values
    Bankruptcy: ClassVar[str] = "Bankruptcy"
    CreditEventUponMerger: ClassVar[str] = "CreditEventUponMerger"
    CrossDefault: ClassVar[str] = "CrossDefault"
    DefaultUnderSpecifiedTransaction: ClassVar[str] = "DefaultUnderSpecifiedTransaction"


# Import after class definition to avoid circular imports
SpecifiedEntityClauseEnum.model_rebuild()
