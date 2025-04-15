"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.schedule.amount_schedule import AmountSchedule
    from src.models.cdm.generated.product.common.schedule.averaging_observation_list import AveragingObservationList
    from src.models.cdm.generated.product.common.schedule.averaging_period import AveragingPeriod
    from src.models.cdm.generated.product.common.schedule.calculation_period import CalculationPeriod
    from src.models.cdm.generated.product.common.schedule.calculation_period_base import CalculationPeriodBase
    from src.models.cdm.generated.product.common.schedule.calculation_period_data import CalculationPeriodData
    from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.date_relative_to_calculation_period_dates import DateRelativeToCalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.date_relative_to_payment_dates import DateRelativeToPaymentDates
    from src.models.cdm.generated.product.common.schedule.date_relative_to_valuation_dates import DateRelativeToValuationDates
    from src.models.cdm.generated.product.common.schedule.final_calculation_period_date_adjustment import FinalCalculationPeriodDateAdjustment
    from src.models.cdm.generated.product.common.schedule.fx_linked_notional_amount import FxLinkedNotionalAmount
    from src.models.cdm.generated.product.common.schedule.fx_linked_notional_schedule import FxLinkedNotionalSchedule
    from src.models.cdm.generated.product.common.schedule.initial_fixing_date import InitialFixingDate
    from src.models.cdm.generated.product.common.schedule.lag import Lag
    from src.models.cdm.generated.product.common.schedule.observation_date import ObservationDate
    from src.models.cdm.generated.product.common.schedule.observation_dates import ObservationDates
    from src.models.cdm.generated.product.common.schedule.observation_schedule import ObservationSchedule
    from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
    from src.models.cdm.generated.product.common.schedule.parametric_dates import ParametricDates
    from src.models.cdm.generated.product.common.schedule.pay_relative_to_enum import PayRelativeToEnum
    from src.models.cdm.generated.product.common.schedule.payment_calculation_period import PaymentCalculationPeriod
    from src.models.cdm.generated.product.common.schedule.payment_date_schedule import PaymentDateSchedule
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.schedule.rate_schedule import RateSchedule
    from src.models.cdm.generated.product.common.schedule.reset_dates import ResetDates
    from src.models.cdm.generated.product.common.schedule.reset_frequency import ResetFrequency
    from src.models.cdm.generated.product.common.schedule.reset_relative_to_enum import ResetRelativeToEnum
    from src.models.cdm.generated.product.common.schedule.stub_calculation_period_amount import StubCalculationPeriodAmount
    from src.models.cdm.generated.product.common.schedule.stub_period import StubPeriod
    from src.models.cdm.generated.product.common.schedule.stub_period_type_enum import StubPeriodTypeEnum
    from src.models.cdm.generated.product.common.schedule.weekly_roll_convention_enum import WeeklyRollConventionEnum
    from src.models.cdm.generated.product.common.schedule.weighted_averaging_observation import WeightedAveragingObservation
