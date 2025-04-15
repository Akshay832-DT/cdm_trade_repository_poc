from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction

class SplitInstruction(CdmModelBase):
    """Specifies instructions for a split, consisting of a breakdown of instructions to be applied to each branch of the split. This instruction can be used to duplicate a trade, as in a clearing scenario, or to split a trade into smaller quantities (in which case each breakdown instruction needs to include a quantity change), as in an allocation."""
    breakdown: List[ForwardRef("PrimitiveInstruction")] = Field(None, description="Each split breakdown specifies the set of primitive instructions to be applied to a single branch of that split. N split breakdowns result in N output trades, which include the original trade. Instructions for how to handle the original trade (e.g. if it must be closed) must be specified in one of the breakdowns.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction
SplitInstruction.model_rebuild()
