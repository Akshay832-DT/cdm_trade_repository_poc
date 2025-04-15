from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction
    from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState

class Instruction(CdmModelBase):
    """Instruction to a function that will be used to perform a business event"""
    primitive_instruction: ForwardRef("PrimitiveInstruction") = Field(None, description="Specifies the primitive instructions that will be used to call primitive event functions.")
    before: ForwardRef("ReferenceWithMetaTradeState") = Field(None, description="Specifies the trade state that will be acted on by the primitive event functions.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction
from src.models.cdm.generated.metafields.reference_with_meta_trade_state import ReferenceWithMetaTradeState
Instruction.model_rebuild()
