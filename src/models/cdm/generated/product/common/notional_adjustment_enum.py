from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class NotionalAdjustmentEnum(CdmModelBase):
    """The enumerated values to specify the conditions that govern the adjustment to the number of units of the return swap."""
    # Enum values
    Execution: ClassVar[str] = "Execution"
    PortfolioRebalancing: ClassVar[str] = "PortfolioRebalancing"
    Standard: ClassVar[str] = "Standard"


# Import after class definition to avoid circular imports
NotionalAdjustmentEnum.model_rebuild()
