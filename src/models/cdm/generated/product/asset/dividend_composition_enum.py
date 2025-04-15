from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendCompositionEnum(CdmModelBase):
    """The enumerated values to specify how the composition of Dividends is to be determined."""
    # Enum values
    CalculationAgentElection: ClassVar[str] = "CalculationAgentElection"
    EquityAmountReceiverElection: ClassVar[str] = "EquityAmountReceiverElection"


# Import after class definition to avoid circular imports
DividendCompositionEnum.model_rebuild()
