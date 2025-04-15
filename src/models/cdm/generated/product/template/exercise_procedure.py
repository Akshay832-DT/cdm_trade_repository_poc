from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.automatic_exercise import AutomaticExercise
    from src.models.cdm.generated.product.template.manual_exercise import ManualExercise

class ExerciseProcedure(CdmModelBase):
    """A class describing how notice of exercise should be given. This can be either manual or automatic."""
    manual_exercise: ForwardRef("ManualExercise") = Field(None, description="Specifies that the notice of exercise must be given by the buyer to the seller or seller's agent.")
    automatic_exercise: ForwardRef("AutomaticExercise") = Field(None, description="If automatic is specified, then the notional amount of the underlying swap not previously exercised under the swaption will be automatically exercised at the expiration time on the expiration date if at such time the buyer is in-the-money, provided that the difference between the settlement rate and the fixed rate under the relevant underlying swap is not less than the specified threshold rate. The term in-the-money is assumed to have the meaning defining in the 2000 ISDA Definitions, Section 17.4 In-the-money.")
    follow_up_confirmation: bool = Field(description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
    limited_right_to_confirm: bool = Field(None, description="Has the meaning defined as part of the 1997 ISDA Government Bond Option Definitions, section 4.5 Limited Right to Confirm Exercise. If present, (i) the Seller may request the Buyer to confirm its intent if not done on or before the expiration time on the Expiration date (ii) specific rules will apply in relation to the settlement mode.")
    split_ticket: bool = Field(None, description="Typically applicable to the physical settlement of bond and convertible bond options. If present, means that the party required to deliver the bonds will divide those to be delivered as notifying party desires to facilitate delivery obligations.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.template.automatic_exercise import AutomaticExercise
from src.models.cdm.generated.product.template.manual_exercise import ManualExercise
ExerciseProcedure.model_rebuild()
