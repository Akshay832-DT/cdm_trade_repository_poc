from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_dates import AdjustableOrRelativeDates
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.product.template.exercise_fee import ExerciseFee
    from src.models.cdm.generated.product.template.exercise_fee_schedule import ExerciseFeeSchedule
    from src.models.cdm.generated.product.template.exercise_procedure import ExerciseProcedure
    from src.models.cdm.generated.product.template.expiration_time_type_enum import ExpirationTimeTypeEnum
    from src.models.cdm.generated.product.template.multiple_exercise import MultipleExercise
    from src.models.cdm.generated.product.template.option_exercise_style_enum import OptionExerciseStyleEnum
    from src.models.cdm.generated.product.template.partial_exercise import PartialExercise

class ExerciseTerms(CdmModelBase):
    """A class defining the exercise period for an option together with any rules governing the notional amount of the underlying which can be exercised on any given exercise date and any associated exercise fees."""
    style: ForwardRef("OptionExerciseStyleEnum") = Field(None, description="Whether the option has a single exercise (european), multiple exercise dates (bermuda), or a continuous range of exercise (american).")
    commencement_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The first day of the exercise period for an American style option.")
    exercise_dates: ForwardRef("AdjustableOrRelativeDates") = Field(None, description="The dates that define the Bermuda option exercise dates and the expiration date. The last specified date is assumed to be the expiration date. The dates can either be specified as a series of explicit dates and associated adjustments or as a series of dates defined relative to another schedule of dates, for example, the calculation period start dates. Where a relative series of dates are defined the first and last possible exercise dates can be separately specified.")
    expiration_date: List[ForwardRef("AdjustableOrRelativeDate")] = Field(None, description="The last day within an exercise period for an American style option. For a European style option it is the only day within the exercise period.")
    relevant_underlying_date: ForwardRef("AdjustableOrRelativeDates") = Field(None, description="The effective date on the underlying product if the option is exercised.  For example, for a swaption it is the swap effective date, for an option on an FX spot or forward it is the value date for settlement, and in an extendible/cancelable provision it is the swap termination date, which is the date on which the termination is effective.'")
    earliest_exercise_time: ForwardRef("BusinessCenterTime") = Field(None, description="The earliest time at which notice of exercise can be given by the buyer to the seller (or seller's agent) to, and including, the expiration date.")
    latest_exercise_time: ForwardRef("BusinessCenterTime") = Field(None, description="For a Bermuda or American style option, the latest time on an exercise business day (excluding the expiration date) within the exercise period that notice can be given by the buyer to the seller or seller's agent. Notice of exercise given after this time will be deemed to have been given on the next exercise business day.")
    expiration_time: ForwardRef("BusinessCenterTime") = Field(None, description="The latest time for exercise on expirationDate. It is made mandatory given that for all option styles, this field is required.")
    expiration_time_type: ForwardRef("ExpirationTimeTypeEnum") = Field(description="The time of day at which the equity option expires, for example the official closing time of the exchange.")
    multiple_exercise: ForwardRef("MultipleExercise") = Field(None, description="As defined in the 2000 ISDA Definitions, Section 12.4. Multiple Exercise, the buyer of the option has the right to exercise all or less than all the unexercised notional amount of the underlying swap on one or more days in the exercise period, but on any such day may not exercise less than the minimum notional amount or more that the maximum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.")
    exercise_fee_schedule: ForwardRef("ExerciseFeeSchedule") = Field(None, description="The fees associated with an exercise date. The fees are conditional on the exercise occurring. The fees can be specified as actual currency amounts or as percentages of the notional amount being exercised.")
    exercise_procedure: ForwardRef("ExerciseProcedure") = Field(None, description="The set of parameters defining the procedure associated with the exercise, e.g. manual exercise.")
    exercise_fee: ForwardRef("ExerciseFee") = Field(None, description="A fee to be paid on exercise. This could be represented as an amount or a rate and notional reference on which to apply the rate.")
    partial_exercise: ForwardRef("PartialExercise") = Field(None, description="As defined in the 2000 ISDA Definitions, Section 12.3. Partial Exercise, the buyer of the option has the right to exercise all or less than all the notional amount of the underlying swap on the expiration date, but may not exercise less than the minimum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.adjustable_or_relative_dates import AdjustableOrRelativeDates
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.product.template.exercise_fee import ExerciseFee
from src.models.cdm.generated.product.template.exercise_fee_schedule import ExerciseFeeSchedule
from src.models.cdm.generated.product.template.exercise_procedure import ExerciseProcedure
from src.models.cdm.generated.product.template.expiration_time_type_enum import ExpirationTimeTypeEnum
from src.models.cdm.generated.product.template.multiple_exercise import MultipleExercise
from src.models.cdm.generated.product.template.option_exercise_style_enum import OptionExerciseStyleEnum
from src.models.cdm.generated.product.template.partial_exercise import PartialExercise
ExerciseTerms.model_rebuild()
