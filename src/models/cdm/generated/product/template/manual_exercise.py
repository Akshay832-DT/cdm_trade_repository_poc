from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice

class ManualExercise(CdmModelBase):
    """A class defining manual exercise, i.e. that the option buyer counterparty must give notice to the option seller of exercise."""
    exercise_notice: ForwardRef("ExerciseNotice") = Field(None, description="Definition of the party to whom notice of exercise should be given.")
    fallback_exercise: bool = Field(None, description="If fallback exercise is specified then the notional amount of the underlying swap, not previously exercised under the swaption, will be automatically exercised at the expiration time on the expiration date if at such time the buyer is in-the-money, provided that the difference between the settlement rate and the fixed rate under the relevant underlying swap is not less than one tenth of a percentage point (0.10% or 0.001). The term in-the-money is assumed to have the meaning defined in the 2000 ISDA Definitions, Section 17.4. In-the-money.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
ManualExercise.model_rebuild()
