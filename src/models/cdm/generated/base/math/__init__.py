"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.arithmetic_operation_enum import ArithmeticOperationEnum
    from src.models.cdm.generated.base.math.averaging_calculation_method import AveragingCalculationMethod
    from src.models.cdm.generated.base.math.averaging_calculation_method_enum import AveragingCalculationMethodEnum
    from src.models.cdm.generated.base.math.averaging_weighting_method_enum import AveragingWeightingMethodEnum
    from src.models.cdm.generated.base.math.capacity_unit_enum import CapacityUnitEnum
    from src.models.cdm.generated.base.math.compare_op import CompareOp
    from src.models.cdm.generated.base.math.dated_value import DatedValue
    from src.models.cdm.generated.base.math.financial_unit_enum import FinancialUnitEnum
    from src.models.cdm.generated.base.math.measure import Measure
    from src.models.cdm.generated.base.math.measure_base import MeasureBase
    from src.models.cdm.generated.base.math.measure_schedule import MeasureSchedule
    from src.models.cdm.generated.base.math.money_bound import MoneyBound
    from src.models.cdm.generated.base.math.money_range import MoneyRange
    from src.models.cdm.generated.base.math.non_negative_quantity import NonNegativeQuantity
    from src.models.cdm.generated.base.math.non_negative_quantity_schedule import NonNegativeQuantitySchedule
    from src.models.cdm.generated.base.math.non_negative_step import NonNegativeStep
    from src.models.cdm.generated.base.math.number_bound import NumberBound
    from src.models.cdm.generated.base.math.number_range import NumberRange
    from src.models.cdm.generated.base.math.quantifier_enum import QuantifierEnum
    from src.models.cdm.generated.base.math.quantity import Quantity
    from src.models.cdm.generated.base.math.quantity_change_direction_enum import QuantityChangeDirectionEnum
    from src.models.cdm.generated.base.math.quantity_schedule import QuantitySchedule
    from src.models.cdm.generated.base.math.rounding import Rounding
    from src.models.cdm.generated.base.math.rounding_direction_enum import RoundingDirectionEnum
    from src.models.cdm.generated.base.math.rounding_mode_enum import RoundingModeEnum
    from src.models.cdm.generated.base.math.schedule import Schedule
    from src.models.cdm.generated.base.math.unit_type import UnitType
    from src.models.cdm.generated.base.math.weather_unit_enum import WeatherUnitEnum
