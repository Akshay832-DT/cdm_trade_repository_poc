from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.valuation import Valuation

class ValuationInstruction(CdmModelBase):
    """Specifies inputs needed to process a valuation."""
    valuation: List[ForwardRef("Valuation")] = Field(None, description="Contains all information related to a valuation.")
    replace: bool = Field(description="Specifies whether the previous valuation tracks in the valuation history are removed (True) or kept (False).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.valuation import Valuation
ValuationInstruction.model_rebuild()
