from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
    from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
    from src.models.cdm.generated.base.datetime.daycount.day_count_fraction_enum import DayCountFractionEnum
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_method_enum import FloatingRateIndexCalculationMethodEnum
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_category_enum import FloatingRateIndexCategoryEnum
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_details import FloatingRateIndexFixingDetails
    from src.models.cdm.generated.observable.asset.fro.floating_rate_index_style_enum import FloatingRateIndexStyleEnum

class FloatingRateIndexCalculationDefaults(CdmModelBase):
    """This holds the rate calculation defaults applicable for a floating rate index."""
    category: ForwardRef("FloatingRateIndexCategoryEnum") = Field(None, description="The ISDA FRO category (e.g. screen rate or calculated rate).")
    index_style: ForwardRef("FloatingRateIndexStyleEnum") = Field(None, description="The ISDA FRO style (e.g. term rate, swap rate, etc).")
    method: ForwardRef("FloatingRateIndexCalculationMethodEnum") = Field(None, description="The ISDA FRO calculation method (e.g. OIS Compounding).")
    fixing: List[ForwardRef("FloatingRateIndexFixingDetails")] = Field(None, description="The default fixing details.")
    day_count_fraction: ForwardRef("DayCountFractionEnum") = Field(None, description="The default day count fraction.")
    applicable_business_days: ForwardRef("BusinessCenters") = Field(None, description="The default applicable business days.")
    publication_calendar: ForwardRef("BusinessCenterEnum") = Field(None, description="Publication Calendar (e.g. EUR-ICESWAP)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
from src.models.cdm.generated.base.datetime.business_centers import BusinessCenters
from src.models.cdm.generated.base.datetime.daycount.day_count_fraction_enum import DayCountFractionEnum
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_calculation_method_enum import FloatingRateIndexCalculationMethodEnum
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_category_enum import FloatingRateIndexCategoryEnum
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_fixing_details import FloatingRateIndexFixingDetails
from src.models.cdm.generated.observable.asset.fro.floating_rate_index_style_enum import FloatingRateIndexStyleEnum
FloatingRateIndexCalculationDefaults.model_rebuild()
