from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
    from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum

class PerformanceValuationDates(CdmModelBase):
    """Defines how and when a performance type option or performance type swap is to be valued."""
    determination_method: ForwardRef("DeterminationMethodEnum") = Field(description="Specifies the method according to which an amount or a date is determined.")
    valuation_dates: ForwardRef("AdjustableRelativeOrPeriodicDates") = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date")
    valuation_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Pricing Date")
    valuation_time: ForwardRef("BusinessCenterTime") = Field(None, description="The specific time of day at which the calculation agent values the underlying. The SpecificTime is the only case when the valuationTime (time + business center location  e.g. 10:00:00 USNY) should be provided. You should be able to provide just the valuationTime without valuationTimeType, which infer that this is a specific time.")
    valuation_time_type: ForwardRef("TimeTypeEnum") = Field(None, description="The time of day at which the calculation agent values the underlying, for example the official closing time of the exchange.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.observable.common.determination_method_enum import DeterminationMethodEnum
from src.models.cdm.generated.observable.common.time_type_enum import TimeTypeEnum
PerformanceValuationDates.model_rebuild()
