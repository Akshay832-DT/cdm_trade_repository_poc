from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
    from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.mandatory_early_termination_adjusted_dates import MandatoryEarlyTerminationAdjustedDates

class MandatoryEarlyTermination(CdmModelBase):
    """A data to:  define an early termination provision for which exercise is mandatory."""
    mandatory_early_termination_date: ForwardRef("AdjustableDate") = Field(description="The early termination date associated with a mandatory early termination of a swap.")
    calculation_agent: ForwardRef("CalculationAgent") = Field(description="The ISDA Calculation Agent responsible for performing duties associated with an optional early termination.")
    cash_settlement: ForwardRef("SettlementTerms") = Field(description="If specified, this means that cash settlement is applicable to the transaction and defines the parameters associated with the cash settlement procedure. If not specified, then physical settlement is applicable.")
    mandatory_early_termination_adjusted_dates: ForwardRef("MandatoryEarlyTerminationAdjustedDates") = Field(None, description="The adjusted dates associated with a mandatory early termination provision. These dates have been adjusted for any applicable business day convention.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_date import AdjustableDate
from src.models.cdm.generated.observable.asset.calculation_agent import CalculationAgent
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.mandatory_early_termination_adjusted_dates import MandatoryEarlyTerminationAdjustedDates
MandatoryEarlyTermination.model_rebuild()
