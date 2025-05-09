"""ISDA CDM models."""
from typing import TYPE_CHECKING

# Import the main classes that need to be exposed
from src.models.cdm.generated.product.template.product import Product
from src.models.cdm.generated.product.template.transferable_product import TransferableProduct
from src.models.cdm.generated.product.template.tradable_product import TradableProduct
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct

if TYPE_CHECKING:
    from src.models.cdm.generated.product.template.asian import Asian
    from src.models.cdm.generated.product.template.asset_leg import AssetLeg
    from src.models.cdm.generated.product.template.asset_payout import AssetPayout
    from src.models.cdm.generated.product.template.asset_payout_trade_type_enum import AssetPayoutTradeTypeEnum
    from src.models.cdm.generated.product.template.automatic_exercise import AutomaticExercise
    from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
    from src.models.cdm.generated.product.template.averaging_in_out_enum import AveragingInOutEnum
    from src.models.cdm.generated.product.template.averaging_strike_feature import AveragingStrikeFeature
    from src.models.cdm.generated.product.template.barrier import Barrier
    from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
    from src.models.cdm.generated.product.template.calendar_spread import CalendarSpread
    from src.models.cdm.generated.product.template.calling_party_enum import CallingPartyEnum
    from src.models.cdm.generated.product.template.cancelable_provision import CancelableProvision
    from src.models.cdm.generated.product.template.cancelable_provision_adjusted_dates import CancelableProvisionAdjustedDates
    from src.models.cdm.generated.product.template.cancellation_event import CancellationEvent
    from src.models.cdm.generated.product.template.composite import Composite
    from src.models.cdm.generated.product.template.constituent_weight import ConstituentWeight
    from src.models.cdm.generated.product.template.dividend_terms import DividendTerms
    from src.models.cdm.generated.product.template.early_termination_event import EarlyTerminationEvent
    from src.models.cdm.generated.product.template.early_termination_provision import EarlyTerminationProvision
    from src.models.cdm.generated.product.template.economic_terms import EconomicTerms
    from src.models.cdm.generated.product.template.evergreen_provision import EvergreenProvision
    from src.models.cdm.generated.product.template.exercise_fee import ExerciseFee
    from src.models.cdm.generated.product.template.exercise_fee_schedule import ExerciseFeeSchedule
    from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
    from src.models.cdm.generated.product.template.exercise_notice_giver_enum import ExerciseNoticeGiverEnum
    from src.models.cdm.generated.product.template.exercise_period import ExercisePeriod
    from src.models.cdm.generated.product.template.exercise_procedure import ExerciseProcedure
    from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
    from src.models.cdm.generated.product.template.expiration_time_type_enum import ExpirationTimeTypeEnum
    from src.models.cdm.generated.product.template.extendible_provision import ExtendibleProvision
    from src.models.cdm.generated.product.template.extendible_provision_adjusted_dates import ExtendibleProvisionAdjustedDates
    from src.models.cdm.generated.product.template.extension_event import ExtensionEvent
    from src.models.cdm.generated.product.template.fixed_price_payout import FixedPricePayout
    from src.models.cdm.generated.product.template.fx_feature import FxFeature
    from src.models.cdm.generated.product.template.knock import Knock
    from src.models.cdm.generated.product.template.mandatory_early_termination import MandatoryEarlyTermination
    from src.models.cdm.generated.product.template.mandatory_early_termination_adjusted_dates import MandatoryEarlyTerminationAdjustedDates
    from src.models.cdm.generated.product.template.manual_exercise import ManualExercise
    from src.models.cdm.generated.product.template.margin_type_enum import MarginTypeEnum
    from src.models.cdm.generated.product.template.multiple_exercise import MultipleExercise
    from src.models.cdm.generated.product.template.option_exercise_style_enum import OptionExerciseStyleEnum
    from src.models.cdm.generated.product.template.option_feature import OptionFeature
    from src.models.cdm.generated.product.template.option_payout import OptionPayout
    from src.models.cdm.generated.product.template.option_strike import OptionStrike
    from src.models.cdm.generated.product.template.option_type_enum import OptionTypeEnum
    from src.models.cdm.generated.product.template.optional_early_termination import OptionalEarlyTermination
    from src.models.cdm.generated.product.template.optional_early_termination_adjusted_dates import OptionalEarlyTerminationAdjustedDates
    from src.models.cdm.generated.product.template.partial_exercise import PartialExercise
    from src.models.cdm.generated.product.template.pass_through import PassThrough
    from src.models.cdm.generated.product.template.pass_through_item import PassThroughItem
    from src.models.cdm.generated.product.template.payout import Payout
    from src.models.cdm.generated.product.template.performance_payout import PerformancePayout
    from src.models.cdm.generated.product.template.portfolio_return_terms import PortfolioReturnTerms
    from src.models.cdm.generated.product.template.quanto import Quanto
    from src.models.cdm.generated.product.template.repo_duration_enum import RepoDurationEnum
    from src.models.cdm.generated.product.template.return_terms import ReturnTerms
    from src.models.cdm.generated.product.template.schedule_period import SchedulePeriod
    from src.models.cdm.generated.product.template.settlement_payout import SettlementPayout
    from src.models.cdm.generated.product.template.strategy_feature import StrategyFeature
    from src.models.cdm.generated.product.template.strike import Strike
    from src.models.cdm.generated.product.template.strike_schedule import StrikeSchedule
    from src.models.cdm.generated.product.template.strike_spread import StrikeSpread
    from src.models.cdm.generated.product.template.termination_provision import TerminationProvision
    from src.models.cdm.generated.product.template.trade_lot import TradeLot
    from src.models.cdm.generated.product.template.underlier import Underlier

__all__ = [
    'Product',
    'TransferableProduct',
    'TradableProduct',
    'NonTransferableProduct'
]
