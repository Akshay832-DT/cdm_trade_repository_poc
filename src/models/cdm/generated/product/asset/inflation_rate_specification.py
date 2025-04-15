from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset
    from src.models.cdm.generated.base.math.averaging_weighting_method_enum import AveragingWeightingMethodEnum
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.metafields.field_with_meta_interpolation_method_enum import FieldWithMetaInterpolationMethodEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
    from src.models.cdm.generated.observable.asset.calculatedrate.fallback_rate_parameters import FallbackRateParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_method_enum import InflationCalculationMethodEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_style_enum import InflationCalculationStyleEnum
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.asset.final_principal_exchange_calculation_enum import FinalPrincipalExchangeCalculationEnum
    from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
    from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
    from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
    from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
    from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule

class InflationRateSpecification(CdmModelBase):
    """A data to:  specify the inflation rate."""
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
    inflation_lag: ForwardRef("Offset") = Field(description="An off-setting period from the payment date which determines the reference period for which the inflation index is observed.")
    index_source: ForwardRef("FieldWithMetaString") = Field(description="The reference source such as Reuters or Bloomberg. FpML specifies indexSource to be of type rateSourcePageScheme, but without specifying actual values.")
    main_publication: ForwardRef("FieldWithMetaString") = Field(description="The current main publication source such as relevant web site or a government body. FpML specifies mainPublication to be of type mainPublicationSource, but without specifying actual values.")
    interpolation_method: ForwardRef("FieldWithMetaInterpolationMethodEnum") = Field(description="The method used when calculating the Inflation Index Level from multiple points. The most common is Linear.")
    initial_index_level: float = Field(None, description="Initial known index level for the first calculation period.")
    fallback_bond_applicable: bool = Field(description="The applicability of a fallback bond as defined in the 2006 ISDA Inflation Derivatives Definitions, sections 1.3 and 1.8.")
    calculation_method: ForwardRef("InflationCalculationMethodEnum") = Field(None, description="Indicates how to use the inflation index to calculate the payment (e.g. Ratio, Return, Spread). Added for Inflation Asset Swap")
    calculation_style: ForwardRef("InflationCalculationStyleEnum") = Field(None, description="Indicates the style of how the inflation index calculates the payment (e.g. YearOnYear, ZeroCoupon).")
    final_principal_exchange_calculation: ForwardRef("FinalPrincipalExchangeCalculationEnum") = Field(None, description="To be specified only for products that embed a redemption payment.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
from src.models.cdm.generated.base.math.averaging_weighting_method_enum import AveragingWeightingMethodEnum
from src.models.cdm.generated.base.math.rounding import Rounding
from src.models.cdm.generated.metafields.field_with_meta_interpolation_method_enum import FieldWithMetaInterpolationMethodEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_interest_rate_index import ReferenceWithMetaInterestRateIndex
from src.models.cdm.generated.observable.asset.calculatedrate.fallback_rate_parameters import FallbackRateParameters
from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_method_enum import InflationCalculationMethodEnum
from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_style_enum import InflationCalculationStyleEnum
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.asset.final_principal_exchange_calculation_enum import FinalPrincipalExchangeCalculationEnum
from src.models.cdm.generated.product.asset.negative_interest_rate_treatment_enum import NegativeInterestRateTreatmentEnum
from src.models.cdm.generated.product.asset.rate_treatment_enum import RateTreatmentEnum
from src.models.cdm.generated.product.asset.spread_schedule import SpreadSchedule
from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule
InflationRateSpecification.model_rebuild()
