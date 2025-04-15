from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
    from src.models.cdm.generated.product.common.schedule.parametric_dates import ParametricDates

class PricingDates(CdmModelBase):
    """Specifies specific dates or parametric rules for the dates on which the price will be determined"""
    specified_dates: List[ForwardRef("AdjustableDates")] = Field(None, description="Defines specified dates on which the price will be determined.")
    parametric_dates: ForwardRef("ParametricDates") = Field(None, description="Defines rules for the dates on which the price will be determined.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_dates import AdjustableDates
from src.models.cdm.generated.product.common.schedule.parametric_dates import ParametricDates
PricingDates.model_rebuild()
