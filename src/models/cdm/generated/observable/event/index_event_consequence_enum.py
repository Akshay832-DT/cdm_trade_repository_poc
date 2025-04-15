from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class IndexEventConsequenceEnum(CdmModelBase):
    """The enumerated values to specify the consequences of Index Events."""
    # Enum values
    CalculationAgentAdjustment: ClassVar[str] = "CalculationAgentAdjustment"
    CancellationAndPayment: ClassVar[str] = "CancellationAndPayment"
    NegotiatedCloseOut: ClassVar[str] = "NegotiatedCloseOut"
    RelatedExchange: ClassVar[str] = "RelatedExchange"


# Import after class definition to avoid circular imports
IndexEventConsequenceEnum.model_rebuild()
