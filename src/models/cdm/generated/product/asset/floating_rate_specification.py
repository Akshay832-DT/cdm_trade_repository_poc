from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.averaging_weighting_method_enum import AveragingWeightingMethodEnum
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
    from src.models.cdm.generated.observable.asset.calculatedrate.fallback_rate_parameters import FallbackRateParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
    from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
    from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
    from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
    from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule

class FloatingRateSpecification(CdmModelBase):
    """A class to specify the floating interest rate by extending the floating rate definition with a set of attributes that specify such rate: the initial value specified as part of the trade, the rounding convention, the averaging method and the negative interest rate treatment."""
    rate_option: ForwardRef("ReferenceWithMetaInterestRateIndex") = Field(None)
    spread_schedule: ForwardRef("SpreadSchedule") = Field(None, description="The ISDA Spread or a Spread schedule expressed as explicit spreads and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The spread is a per annum rate, expressed as a decimal. For purposes of determining a calculation period amount, if positive the spread will be added to the floating rate and if negative the spread will be subtracted from the floating rate. A positive 10 basis point (0.1%) spread would be represented as 0.001.")
    cap_rate_schedule: ForwardRef("StrikeSchedule") = Field(None, description="The cap rate or cap rate schedule, if any, which applies to the floating rate. The cap rate (strike) is only required where the floating rate on a swap stream is capped at a certain level. A cap rate schedule is expressed as explicit cap rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The cap rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A cap rate of 5% would be represented as 0.05.")
    floor_rate_schedule: ForwardRef("StrikeSchedule") = Field(None, description="The floor rate or floor rate schedule, if any, which applies to the floating rate. The floor rate (strike) is only required where the floating rate on a swap stream is floored at a certain strike level. A floor rate schedule is expressed as explicit floor rates and dates and the step dates may be subject to adjustment in accordance with any adjustments specified in calculationPeriodDatesAdjustments. The floor rate is assumed to be exclusive of any spread and is a per annum rate, expressed as a decimal. A floor rate of 5% would be represented as 0.05.")
    floating_rate_multiplier_schedule: ForwardRef("RateSchedule") = Field(None, description="A rate multiplier or multiplier schedule to apply to the floating rate. A multiplier schedule is expressed as explicit multipliers and dates. In the case of a schedule, the step dates may be subject to adjustment in accordance with any adjustments specified in the calculationPeriodDatesAdjustments. The multiplier can be a positive or negative decimal. This element should only be included if the multiplier is not equal to 1 (one) for the term of the stream.")
    rate_treatment: ForwardRef("RateTreatmentEnum") = Field(None, description="The specification of any rate conversion which needs to be applied to the observed rate before being used in any calculations. The two common conversions are for securities quoted on a bank discount basis which will need to be converted to either a Money Market Yield or Bond Equivalent Yield. See the Annex to the 2000 ISDA Definitions, Section 7.3. Certain General Definitions Relating to Floating Rate Options, paragraphs (g) and (h) for definitions of these terms.")
    calculation_parameters: ForwardRef("FloatingRateCalculationParameters") = Field(None, description="Support for modular calculated rates, such such as lockout compound calculations.")
    fallback_rate: ForwardRef("FallbackRateParameters") = Field(None, description="Definition of any fallback rate that may be applicable.")
    initial_rate: ForwardRef("Price") = Field(None, description="The initial floating rate reset agreed between the principal parties involved in the trade. This is assumed to be the first required reset rate for the first regular calculation period. It should only be included when the rate is not equal to the rate published on the source implied by the floating rate index. An initial rate of 5% would be represented as 0.05.")
    final_rate_rounding: ForwardRef("Rounding") = Field(None, description="The rounding convention to apply to the final rate used in determination of a calculation period amount.")
    averaging_method: ForwardRef("AveragingWeightingMethodEnum") = Field(None, description="If averaging is applicable, this component specifies whether a weighted or unweighted average method of calculation is to be used. The component must only be included when averaging applies.")
    negative_interest_rate_treatment: ForwardRef("NegativeInterestRateTreatmentEnum") = Field(None, description="The specification of any provisions for calculating payment obligations when a floating rate is negative (either due to a quoted negative floating rate or by operation of a spread that is subtracted from the floating rate).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.averaging_weighting_method_enum import AveragingWeightingMethodEnum
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
from src.models.cdm.generated.observable.asset.calculatedrate.fallback_rate_parameters import FallbackRateParameters
from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule
FloatingRateSpecification.model_rebuild()
