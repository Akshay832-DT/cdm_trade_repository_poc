from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.common.contract_formation_instruction import ContractFormationInstruction
    from src.models.cdm.generated.event.common.execution_instruction import ExecutionInstruction
    from src.models.cdm.generated.event.common.exercise_instruction import ExerciseInstruction
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

class PrimitiveInstruction(CdmModelBase):
    """A Primitive Instruction describes the inputs required to pass into the corresponding PrimitiveEvent function."""
    contract_formation: ForwardRef("ContractFormationInstruction") = Field(None, description="Specifies instructions describing an contract formation primitive event.")
    execution: ForwardRef("ExecutionInstruction") = Field(None, description="Specifies instructions describing an execution primitive event.")
    exercise: ForwardRef("ExerciseInstruction") = Field(None, description="Specifies instructions describing an exercise primitive event.")
    party_change: ForwardRef("PartyChangeInstruction") = Field(None, description="Specifies instructions describing a party change primitive event.")
    quantity_change: ForwardRef("QuantityChangeInstruction") = Field(None, description="Specifies instructions describing an quantity change primitive event.")
    reset: ForwardRef("ResetInstruction") = Field(None, description="Specifies instructions describing a reset event.")
    split: ForwardRef("SplitInstruction") = Field(None, description="Specifies instructions to split a trade into multiple branches.")
    terms_change: ForwardRef("TermsChangeInstruction") = Field(None, description="Specifies instructions describing a terms change primitive event.")
    transfer: ForwardRef("TransferInstruction") = Field(None, description="Specifies instructions describing a transfer primitive event.")
    index_transition: ForwardRef("IndexTransitionInstruction") = Field(None, description="Specifies inputs needed to process a Index Transition business event.")
    stock_split: ForwardRef("StockSplitInstruction") = Field(None, description="Specifies inputs needed to process a Stock Split business event.")
    observation: ForwardRef("ObservationInstruction") = Field(None, description="Specifies inputs needed to process an observation.")
    valuation: ForwardRef("ValuationInstruction") = Field(None, description="Specifies inputs needed to process an update of a valuation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.common.contract_formation_instruction import ContractFormationInstruction
from src.models.cdm.generated.event.common.execution_instruction import ExecutionInstruction
from src.models.cdm.generated.event.common.exercise_instruction import ExerciseInstruction
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
PrimitiveInstruction.model_rebuild()
