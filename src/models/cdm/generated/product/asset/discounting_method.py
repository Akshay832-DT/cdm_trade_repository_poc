from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_day_count_fraction_enum import FieldWithMetaDayCountFractionEnum
    from src.models.cdm.generated.product.asset.discounting_type_enum import DiscountingTypeEnum

class DiscountingMethod(CdmModelBase):
    """A data defining:  discounting information. The 2000 ISDA definitions, section 8.4. discounting (related to the calculation of a discounted fixed amount or floating amount) apply. This type must only be included if discounting applies."""
    discounting_type: ForwardRef("DiscountingTypeEnum") = Field(description="The discounting method that is applicable.")
    discount_rate: float = Field(None, description="A discount rate, expressed as a decimal, to be used in the calculation of a discounted amount. A discount amount of 5% would be represented as 0.05.")
    discount_rate_day_count_fraction: ForwardRef("FieldWithMetaDayCountFractionEnum") = Field(None, description="A discount day count fraction to be used in the calculation of a discounted amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_day_count_fraction_enum import FieldWithMetaDayCountFractionEnum
from src.models.cdm.generated.product.asset.discounting_type_enum import DiscountingTypeEnum
DiscountingMethod.model_rebuild()
