from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.buyer_seller import BuyerSeller
    from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
    from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
    from src.models.cdm.generated.product.template.optional_early_termination_adjusted_dates import OptionalEarlyTerminationAdjustedDates

class OptionalEarlyTermination(CdmModelBase):
    """A data defining:  an early termination provision where either or both parties have the right to exercise."""
    single_party_option: ForwardRef("BuyerSeller") = Field(None, description="If optional early termination is not available to both parties then this component specifies the buyer and seller of the option. In FpML, this attribute is of type SinglePsrtyOption, which actually consists of the BuyerSeller.model.")
    mutual_early_termination: bool = Field(None, description="Used for specifying whether the Mutual Early Termination Right that is detailed in the Master Confirmation will apply.")
    exercise_notice: List[ForwardRef("ExerciseNotice")] = Field(None, description="Definition of the party to whom notice of exercise should be given.")
    follow_up_confirmation: bool = Field(None, description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
    calculation_agent: ForwardRef("CalculationAgent") = Field(None, description="The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.")
    cash_settlement: ForwardRef("SettlementTerms") = Field(None, description="If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.")
    optional_early_termination_adjusted_dates: ForwardRef("OptionalEarlyTerminationAdjustedDates") = Field(None, description="An early termination provision to terminate the trade at fair value where one or both parties have the right to decide on termination.")
    exercise_terms: ForwardRef("ExerciseTerms") = Field(description="The exercise terms associated with the optional early termination, including details such as exercise style, exercise fees, and any other relevant conditions or terms.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.buyer_seller import BuyerSeller
from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
from src.models.cdm.generated.product.template.optional_early_termination_adjusted_dates import OptionalEarlyTerminationAdjustedDates
OptionalEarlyTermination.model_rebuild()
