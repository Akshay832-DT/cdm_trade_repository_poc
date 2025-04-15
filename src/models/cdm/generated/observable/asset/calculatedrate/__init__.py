"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_details import CalculatedRateDetails
    from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_observation_dates_and_weights import CalculatedRateObservationDatesAndWeights
    from src.models.cdm.generated.observable.asset.calculatedrate.calculated_rate_observations import CalculatedRateObservations
    from src.models.cdm.generated.observable.asset.calculatedrate.calculation_method_enum import CalculationMethodEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.calculation_shift_method_enum import CalculationShiftMethodEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.fallback_rate_parameters import FallbackRateParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.floating_rate_calculation_parameters import FloatingRateCalculationParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_method_enum import InflationCalculationMethodEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.inflation_calculation_style_enum import InflationCalculationStyleEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_parameters import ObservationParameters
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_period_dates_enum import ObservationPeriodDatesEnum
    from src.models.cdm.generated.observable.asset.calculatedrate.observation_shift_calculation import ObservationShiftCalculation
    from src.models.cdm.generated.observable.asset.calculatedrate.offset_calculation import OffsetCalculation
