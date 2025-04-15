from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney

class MultipleExercise(CdmModelBase):
    """A class defining multiple exercises. As defined in the 2000 ISDA Definitions, Section 12.4. Multiple Exercise, the buyer of the option has the right to exercise all or less than all the unexercised notional amount of the underlying swap on one or more days in the exercise period, but on any such day may not exercise less than the minimum notional amount or more than the maximum notional amount, and if an integral multiple amount is specified, the notional exercised must be equal to or, be an integral multiple of, the integral multiple amount. In FpML, MultipleExercise is built upon the PartialExercise.model."""
    notiona_reference: ForwardRef("ReferenceWithMetaMoney") = Field(None, description="A pointer style reference to the associated notional schedule defined elsewhere in the document. This element has been made optional as part of its integration in the OptionBaseExtended, because not required for the options on securities.")
    integral_multiple_amount: float = Field(None, description="A notional amount which restricts the amount of notional that can be exercised when partial exercise or multiple exercise is applicable. The integral multiple amount defines a lower limit of notional that can be exercised and also defines a unit multiple of notional that can be exercised, i.e. only integer multiples of this amount can be exercised.")
    minimum_notional_amount: float = Field(None, description="The minimum notional amount that can be exercised on a given exercise date. See multipleExercise.")
    minimum_number_of_options: int = Field(None, description="The minimum number of options that can be exercised on a given exercise date.")
    maximum_notional_amount: float = Field(None, description="The maximum notional amount that can be exercised on a given exercise date.")
    maximum_number_of_options: int = Field(None, description="The maximum number of options that can be exercised on a given exercise date. If the number is not specified, it means that the maximum number of options corresponds to the remaining unexercised options.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney
MultipleExercise.model_rebuild()
