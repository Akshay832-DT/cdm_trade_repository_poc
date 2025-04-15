from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.base.math.schedule import Schedule
    from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
    from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
    from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
    from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule

class StubFloatingRate(CdmModelBase):
    """A class defining a floating rate."""
    floating_rate_index: ForwardRef("FloatingRateIndexEnum") = Field(description="The floating rate index.")
    index_tenor: ForwardRef("Period") = Field(None, description="The ISDA Designated Maturity, i.e. the tenor of the floating rate.")
    floating_rate_multiplier_schedule: ForwardRef("Schedule") = Field(None, description="A rate multiplier or multiplier schedule to apply to the floating rate. A multiplier schedule is expressed as explicit multipliers and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in the calculationPeriodDatesAdjustments. The multiplier can be a positive or negative decimal. This element should only be included if the multiplier is not equal to 1 (one) for the term of the stream.")
    spread_schedule: List[ForwardRef("SpreadSchedule")] = Field(None, description="The ISDA Spread or a Spread schedule expressed as explicit spreads and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.")
    rate_treatment: ForwardRef("RateTreatmentEnum") = Field(None, description="The specification of any rate conversion which needs to be applied to the observed rate before being used in any calculations. The two common conversions are for securities quoted on a bank discount basis which will need to be converted to either a Money Market Yield or Bond Equivalent Yield. See the Annex to the 2000 ISDA Definitions, Section 7.3. Certain General Definitions Relating to Floating Rate Options, paragraphs (g) and (h) for definitions of these terms.")
    cap_rate_schedule: List[ForwardRef("StrikeSchedule")] = Field(None, description="The cap rate or cap rate schedule, if any, which applies to the floating rate. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain level. A cap rate schedule is expressed as explicit cap rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.")
    floor_rate_schedule: List[ForwardRef("StrikeSchedule")] = Field(None, description="The floor rate or floor rate schedule, if any, which applies to the floating rate. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. A floor rate schedule is expressed as explicit floor rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A floor rate of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.base.math.schedule import Schedule
from src.models.cdm.generated.base.staticdata.asset.rates.floating_rate_index_enum import FloatingRateIndexEnum
from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule
StubFloatingRate.model_rebuild()
