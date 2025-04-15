from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuotationRateTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of quotation rate to be obtained from each cash settlement reference bank."""
    # Enum values
    Ask: ClassVar[str] = "Ask"
    Bid: ClassVar[str] = "Bid"
    ExercisingPartyPays: ClassVar[str] = "ExercisingPartyPays"
    Mid: ClassVar[str] = "Mid"


# Import after class definition to avoid circular imports
QuotationRateTypeEnum.model_rebuild()
