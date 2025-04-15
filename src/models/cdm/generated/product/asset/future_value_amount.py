from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule

class FutureValueAmount(CdmModelBase):
    """A class defining a currency and a future value date."""
    quantity: ForwardRef("ReferenceWithMetaNonNegativeQuantitySchedule") = Field(None)
    currency: ForwardRef("FieldWithMetaString") = Field(description="The currency in which the an amount is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    calculation_period_number_of_days: int = Field(description="The number of days from the adjusted calculation period start date to the adjusted value date, calculated in accordance with the applicable day count fraction.")
    value_date: str = Field(description="Adjusted value date of the future value amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_non_negative_quantity_schedule import ReferenceWithMetaNonNegativeQuantitySchedule
FutureValueAmount.model_rebuild()
