from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.interpolation_method_enum import InterpolationMethodEnum
    from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum

class MakeWholeAmount(CdmModelBase):
    """A class to specify the amount to be paid by the buyer of the option if the option is exercised prior to the Early Call Date (typically applicable to the convertible bond options)."""
    floating_rate_index: ForwardRef("FloatingRateIndexEnum") = Field(None)
    index_tenor: ForwardRef("Period") = Field(None, description="The ISDA Designated Maturity, i.e. the tenor of the floating rate.")
    spread: float = Field(None, description="Spread in basis points over the floating rate index.")
    side: ForwardRef("QuotationSideEnum") = Field(None, description="The side (bid/mid/ask) of the measure.")
    interpolation_method: ForwardRef("InterpolationMethodEnum") = Field(None, description="The type of interpolation method that the calculation agent reserves the right to use.")
    early_call_date: ForwardRef("FieldWithMetaString") = Field(description="Date prior to which the option buyer will have to pay a Make Whole Amount to the option seller if he/she exercises the option.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.interpolation_method_enum import InterpolationMethodEnum
from src.models.cdm.generated.observable.asset.quotation_side_enum import QuotationSideEnum
MakeWholeAmount.model_rebuild()
