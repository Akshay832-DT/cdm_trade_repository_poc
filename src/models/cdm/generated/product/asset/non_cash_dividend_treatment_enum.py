from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NonCashDividendTreatmentEnum(CdmModelBase):
    """The enumerated values to specify the treatment of Non-Cash Dividends."""
    # Enum values
    CashEquivalent: ClassVar[str] = "CashEquivalent"
    PotentialAdjustmentEvent: ClassVar[str] = "PotentialAdjustmentEvent"


# Import after class definition to avoid circular imports
NonCashDividendTreatmentEnum.model_rebuild()
