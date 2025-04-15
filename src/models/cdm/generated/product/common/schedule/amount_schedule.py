from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.dated_value import DatedValue
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class AmountSchedule(CdmModelBase):
    """A class to specify a currency amount or a currency amount schedule."""
    value: float = Field(None, description="The initial rate or amount, as the case may be. An initial rate of 5% would be represented as 0.05.")
    dated_value: List[ForwardRef("DatedValue")] = Field(None, description="The schedule of step date and value pairs. On each step date the associated step value becomes effective. A list of steps may be ordered in the document by ascending step date. An FpML document containing an unordered list of steps is still regarded as a conformant document.")
    currency: List[ForwardRef("FieldWithMetaString")] = Field(None, description="The currency in which the amount schedule is denominated. The currency is specified outside of the actual schedule in order to be applied uniformly to it. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.dated_value import DatedValue
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
AmountSchedule.model_rebuild()
