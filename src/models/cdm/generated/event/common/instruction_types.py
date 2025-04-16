"""
This module contains type definitions for instruction types to avoid circular dependencies.
"""
from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

from src.models.cdm.generated.event.common.instruction_models import ExerciseInstruction, PrimitiveInstruction

# Create forward references for instruction types
ContractFormationInstructionRef = ForwardRef("ContractFormationInstruction")
ExecutionInstructionRef = ForwardRef("ExecutionInstruction")
ExerciseInstructionRef = ForwardRef("ExerciseInstruction")
IndexTransitionInstructionRef = ForwardRef("IndexTransitionInstruction")
ObservationInstructionRef = ForwardRef("ObservationInstruction")
PartyChangeInstructionRef = ForwardRef("PartyChangeInstruction")
QuantityChangeInstructionRef = ForwardRef("QuantityChangeInstruction")
ResetInstructionRef = ForwardRef("ResetInstruction")
SplitInstructionRef = ForwardRef("SplitInstruction")
StockSplitInstructionRef = ForwardRef("StockSplitInstruction")
TermsChangeInstructionRef = ForwardRef("TermsChangeInstruction")
TransferInstructionRef = ForwardRef("TransferInstruction")
ValuationInstructionRef = ForwardRef("ValuationInstruction")
PrimitiveInstructionRef = ForwardRef("PrimitiveInstruction")

# Import dependencies after class definition
if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.execution_instruction import ExecutionInstruction
    from src.models.cdm.generated.event.common.index_transition_instruction import IndexTransitionInstruction
    from src.models.cdm.generated.event.common.observation_instruction import ObservationInstruction
    from src.models.cdm.generated.event.common.party_change_instruction import PartyChangeInstruction
    from src.models.cdm.generated.event.common.quantity_change_instruction import QuantityChangeInstruction
    from src.models.cdm.generated.event.common.reset_instruction import ResetInstruction
    from src.models.cdm.generated.event.common.split_instruction import SplitInstruction
    from src.models.cdm.generated.event.common.stock_split_instruction import StockSplitInstruction
    from src.models.cdm.generated.event.common.terms_change_instruction import TermsChangeInstruction
    from src.models.cdm.generated.event.common.transfer_instruction import TransferInstruction
    from src.models.cdm.generated.event.common.valuation_instruction import ValuationInstruction 