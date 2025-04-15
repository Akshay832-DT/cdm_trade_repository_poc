from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney

class PartialExercise(CdmModelBase):
    """A class defining partial exercise. As defined in the 2000 ISDA Definitions, Section 12.3 Partial Exercise, the buyer of the option may exercise all or less than all the notional amount of the underlying swap but may not be less than the minimum notional amount (if specified) and must be an integral multiple of the integral multiple amount if specified."""
    notiona_reference: ForwardRef("ReferenceWithMetaMoney") = Field(description="A pointer style reference to the associated notional schedule defined elsewhere in the document. This element has been made optional as part of its integration in the OptionBaseExtended, because not required for the options on securities.")
    integral_multiple_amount: float = Field(None, description="A notional amount which restricts the amount of notional that can be exercised when partial exercise or multiple exercise is applicable. The integral multiple amount defines a lower limit of notional that can be exercised and also defines a unit multiple of notional that can be exercised, i.e. only integer multiples of this amount can be exercised.")
    minimum_notional_amount: float = Field(None, description="The minimum notional amount that can be exercised on a given exercise date. See multipleExercise.")
    minimum_number_of_options: int = Field(None, description="The minimum number of options that can be exercised on a given exercise date.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_money import ReferenceWithMetaMoney
PartialExercise.model_rebuild()
