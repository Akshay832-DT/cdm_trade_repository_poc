from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
    from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
    from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule

class FloatingRateBase(CdmModelBase):
    """A class defining a floating interest rate through the specification of the floating rate index, the tenor, the multiplier schedule, the spread, the qualification of whether a specific rate treatment and/or a cap or floor apply."""
    rate_option: ForwardRef("ReferenceWithMetaInterestRateIndex") = Field(None)
    spread_schedule: ForwardRef("SpreadSchedule") = Field(None, description="The ISDA Spread or a Spread schedule expressed as explicit spreads and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.")
    cap_rate_schedule: ForwardRef("StrikeSchedule") = Field(None, description="The cap rate or cap rate schedule, if any, which applies to the floating rate. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain level. A cap rate schedule is expressed as explicit cap rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.")
    floor_rate_schedule: ForwardRef("StrikeSchedule") = Field(None, description="The floor rate or floor rate schedule, if any, which applies to the floating rate. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. A floor rate schedule is expressed as explicit floor rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A floor rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule
FloatingRateBase.model_rebuild()
