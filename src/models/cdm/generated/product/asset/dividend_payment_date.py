from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_adjustable_or_relative_date import ReferenceWithMetaAdjustableOrRelativeDate
    from src.models.cdm.generated.product.asset.dividend_date_reference import DividendDateReference

class DividendPaymentDate(CdmModelBase):
    """A class describing the date on which the dividend will be paid/received. This class is also used to specify the date on which the FX rate will be determined, when applicable."""
    dividend_date_reference: ForwardRef("DividendDateReference") = Field(None)
    dividend_date: ForwardRef("ReferenceWithMetaAdjustableOrRelativeDate") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_adjustable_or_relative_date import ReferenceWithMetaAdjustableOrRelativeDate
from src.models.cdm.generated.product.asset.dividend_date_reference import DividendDateReference
DividendPaymentDate.model_rebuild()
