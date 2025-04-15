from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ShareExtraordinaryEventEnum(CdmModelBase):
    """The enumerated values to specify the consequences of extraordinary events relating to the underlying."""
    # Enum values
    AlternativeObligation: ClassVar[str] = "AlternativeObligation"
    CalculationAgent: ClassVar[str] = "CalculationAgent"
    CancellationAndPayment: ClassVar[str] = "CancellationAndPayment"
    Component: ClassVar[str] = "Component"
    ModifiedCalculationAgent: ClassVar[str] = "ModifiedCalculationAgent"
    OptionsExchange: ClassVar[str] = "OptionsExchange"
    PartialCancellationAndPayment: ClassVar[str] = "PartialCancellationAndPayment"


# Import after class definition to avoid circular imports
ShareExtraordinaryEventEnum.model_rebuild()
