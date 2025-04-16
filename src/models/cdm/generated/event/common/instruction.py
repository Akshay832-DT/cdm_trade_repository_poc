from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

from src.models.cdm.generated.event.common.instruction_models import PrimitiveInstruction

class Instruction(CdmModelBase):
    """A class to specify the instructions that form part of a business event."""
    primitive: Optional[PrimitiveInstruction] = Field(None, description="Specifies the primitive instruction that forms part of a business event.")

# Import dependencies after class definition
if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.instruction_models import PrimitiveInstruction

# Rebuild this model
Instruction.model_rebuild()
