from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantity import Quantity

class ReturnInstruction(CdmModelBase):
    """Specifies the information required to create the return of a Security Finance Transaction."""
    quantity: List[ForwardRef("Quantity")] = Field(None, description="Specifies the quantity of shares and cash to be returned in a partial return event.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantity import Quantity
ReturnInstruction.model_rebuild()
