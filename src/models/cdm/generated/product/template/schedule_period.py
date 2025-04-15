from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.date_range import DateRange
    from src.models.cdm.generated.product.asset.calculation_schedule_delivery_periods import CalculationScheduleDeliveryPeriods

class SchedulePeriod(CdmModelBase):
    """A class that defines the period of a schedule. The period contains a set of start and end dates, quantities, fixing, and pricing data."""
    calculation_period: ForwardRef("DateRange") = Field(description="Period for which the payment is generated.")
    payment_date: str = Field(description="Adjusted payment date.")
    fixing_period: ForwardRef("DateRange") = Field(description="Period over which the underlying price is observed.")
    delivery_period: ForwardRef("CalculationScheduleDeliveryPeriods") = Field(None, description="Period and time profile over which the delivery takes place.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.date_range import DateRange
from src.models.cdm.generated.product.asset.calculation_schedule_delivery_periods import CalculationScheduleDeliveryPeriods
SchedulePeriod.model_rebuild()
