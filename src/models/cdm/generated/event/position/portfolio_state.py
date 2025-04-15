from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.lineage import Lineage
    from src.models.cdm.generated.event.position.position import Position

class PortfolioState(CdmModelBase):
    """State-full representation of a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state"""
    positions: List[ForwardRef("Position")] = Field(None, description="The list of positions, each containing a Quantity and a Product.")
    lineage: ForwardRef("Lineage") = Field(description="Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.lineage import Lineage
from src.models.cdm.generated.event.position.position import Position
PortfolioState.model_rebuild()
