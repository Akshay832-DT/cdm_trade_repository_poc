from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class StandardSettlementStyleEnum(CdmModelBase):
    """The enumerated values to specify whether a trade is settling using standard settlement instructions as well as whether it is a candidate for settlement netting."""
    # Enum values
    Net: ClassVar[str] = "Net"
    PairAndNet: ClassVar[str] = "PairAndNet"
    Standard: ClassVar[str] = "Standard"
    StandardAndNet: ClassVar[str] = "StandardAndNet"


# Import after class definition to avoid circular imports
StandardSettlementStyleEnum.model_rebuild()
