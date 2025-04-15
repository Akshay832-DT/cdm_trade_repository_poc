from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.product.template.exercise_period import ExercisePeriod
    from src.models.cdm.generated.product.template.mandatory_early_termination import MandatoryEarlyTermination
    from src.models.cdm.generated.product.template.optional_early_termination import OptionalEarlyTermination

class EarlyTerminationProvision(CdmModelBase):
    """A data defining:  an early termination provision for a swap. This early termination is at fair value, i.e. on termination the fair value of the product must be settled between the parties."""
    mandatory_early_termination: ForwardRef("MandatoryEarlyTermination") = Field(None, description="A mandatory early termination provision to terminate the swap at fair value.")
    mandatory_early_termination_date_tenor: ForwardRef("Period") = Field(None, description="Period after trade date of the mandatory early termination date.")
    optional_early_termination: ForwardRef("OptionalEarlyTermination") = Field(None, description="An option for either or both parties to terminate the swap at fair value.")
    optional_early_termination_parameters: ForwardRef("ExercisePeriod") = Field(None, description="Definition of the first early termination date and the frequency of the termination dates subsequent to that. American exercise is defined by having a frequency of one day.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.product.template.exercise_period import ExercisePeriod
from src.models.cdm.generated.product.template.mandatory_early_termination import MandatoryEarlyTermination
from src.models.cdm.generated.product.template.optional_early_termination import OptionalEarlyTermination
EarlyTerminationProvision.model_rebuild()
