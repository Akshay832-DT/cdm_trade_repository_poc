"""ISDA CDM instruction models."""
from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

# Import dependencies first
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_date import AdjustableOrAdjustedDate
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from src.models.cdm.generated.metafields.reference_with_meta_option_payout import ReferenceWithMetaOptionPayout
from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
from src.models.cdm.generated.event.common.execution_instruction import ExecutionInstruction
from src.models.cdm.generated.event.common.party_change_instruction import PartyChangeInstruction
from src.models.cdm.generated.event.common.quantity_change_instruction import QuantityChangeInstruction
from src.models.cdm.generated.event.common.reset_instruction import ResetInstruction
from src.models.cdm.generated.event.common.terms_change_instruction import TermsChangeInstruction
from src.models.cdm.generated.event.common.transfer_instruction import TransferInstruction
from src.models.cdm.generated.event.common.index_transition_instruction import IndexTransitionInstruction
from src.models.cdm.generated.event.common.stock_split_instruction import StockSplitInstruction
from src.models.cdm.generated.event.common.observation_instruction import ObservationInstruction
from src.models.cdm.generated.event.common.valuation_instruction import ValuationInstruction

# Rebuild dependencies first
AdjustableOrAdjustedDate.model_rebuild()
BusinessCenterTime.model_rebuild()
TradeIdentifier.model_rebuild()
ReferenceWithMetaOptionPayout.model_rebuild()
LegalAgreement.model_rebuild()
ExecutionInstruction.model_rebuild()
PartyChangeInstruction.model_rebuild()
QuantityChangeInstruction.model_rebuild()
ResetInstruction.model_rebuild()
TermsChangeInstruction.model_rebuild()
TransferInstruction.model_rebuild()
IndexTransitionInstruction.model_rebuild()
StockSplitInstruction.model_rebuild()
ObservationInstruction.model_rebuild()
ValuationInstruction.model_rebuild()

class ContractFormationInstruction(CdmModelBase):
    """Specifies instructions to create a fully formed contract, with optional legal agreements."""
    legal_agreement: Optional[List["LegalAgreement"]] = Field(None, description="Optional legal agreements associated to the contract being formed, for instance a master agreement.")

class PrimitiveInstruction(CdmModelBase):
    """A Primitive Instruction describes the inputs required to pass into the corresponding PrimitiveEvent function."""
    contract_formation: Optional["ContractFormationInstruction"] = Field(None, description="Specifies instructions describing an contract formation primitive event.")
    execution: Optional["ExecutionInstruction"] = Field(None, description="Specifies instructions describing an execution primitive event.")
    exercise: Optional["ExerciseInstruction"] = Field(None, description="Specifies instructions describing an exercise primitive event.")
    party_change: Optional["PartyChangeInstruction"] = Field(None, description="Specifies instructions describing a party change primitive event.")
    quantity_change: Optional["QuantityChangeInstruction"] = Field(None, description="Specifies instructions describing an quantity change primitive event.")
    reset: Optional["ResetInstruction"] = Field(None, description="Specifies instructions describing a reset event.")
    split: Optional["SplitInstruction"] = Field(None, description="Specifies instructions to split a trade into multiple branches.")
    terms_change: Optional["TermsChangeInstruction"] = Field(None, description="Specifies instructions describing a terms change primitive event.")
    transfer: Optional["TransferInstruction"] = Field(None, description="Specifies instructions describing a transfer primitive event.")
    index_transition: Optional["IndexTransitionInstruction"] = Field(None, description="Specifies inputs needed to process a Index Transition business event.")
    stock_split: Optional["StockSplitInstruction"] = Field(None, description="Specifies inputs needed to process a Stock Split business event.")
    observation: Optional["ObservationInstruction"] = Field(None, description="Specifies inputs needed to process an observation.")
    valuation: Optional["ValuationInstruction"] = Field(None, description="Specifies inputs needed to process an update of a valuation.")

class SplitInstruction(CdmModelBase):
    """A class to specify the instructions for splitting a trade into multiple branches."""
    primitive: Optional[List["PrimitiveInstruction"]] = Field(None, description="Specifies the primitive instructions for each branch of the split.")

class ExerciseInstruction(CdmModelBase):
    """Specifies the information required to communicate the choices made by the exercising party, in a financial product endowing the party with at least one option."""
    exercise_quantity: PrimitiveInstruction = Field(description="Contains instructions for exercising the option including a quantity change, and optionally a transfer.")
    exercise_option: Optional["ReferenceWithMetaOptionPayout"] = Field(None, description="Specifies the Option Payout being exercised on the trade.")
    exercise_date: Optional["AdjustableOrAdjustedDate"] = Field(None, description="Specifies the date on which an option contained within the financial product would be exercised. The date may be omitted if the contractual product allows for only a single date of exercise (European exercise).")
    exercise_time: Optional["BusinessCenterTime"] = Field(None, description="Specifies the time at which an option contained within the financial product woulld be exercised. The time may be omitted if the contractual product allows for only a single time of exercise (European exercise). ")
    replacement_trade_identifier: Optional[List["TradeIdentifier"]] = Field(None, description="Specifies the trade identifier to apply to the replacement trade for physical exercise.")

# Rebuild the models
ContractFormationInstruction.model_rebuild()
PrimitiveInstruction.model_rebuild()
SplitInstruction.model_rebuild()
ExerciseInstruction.model_rebuild() 