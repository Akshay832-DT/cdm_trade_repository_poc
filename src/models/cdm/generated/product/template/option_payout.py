from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.buyer_seller import BuyerSeller
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
    from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
    from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
    from src.models.cdm.generated.product.template.option_feature import OptionFeature
    from src.models.cdm.generated.product.template.option_strike import OptionStrike
    from src.models.cdm.generated.product.template.option_type_enum import OptionTypeEnum
    from src.models.cdm.generated.product.template.underlier import Underlier

class OptionPayout(CdmModelBase):
    """ The option payout specification terms. The associated globalKey denotes the ability to associate a hash value to the respective OptionPayout instantiation for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    buyer_seller: ForwardRef("BuyerSeller") = Field()
    feature: ForwardRef("OptionFeature") = Field(None, description="The option feature, such as quanto, Asian, barrier, knock.")
    observation_terms: ForwardRef("ObservationTerms") = Field(None, description="Class containing terms that are associated with observing a price/benchmark/index across either single or multple observations. To be used for option contracts that reference a benchmark price.")
    schedule: ForwardRef("CalculationSchedule") = Field(None, description="Allows the full representation of a payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")
    delivery: ForwardRef("AssetDeliveryInformation") = Field(None, description="Contains the information relative to the delivery of the asset.")
    underlier: ForwardRef("Underlier") = Field(description="The financial product underlying the option, which can be of any type including an Asset, Basket, Index or a NonTransferableProduct.")
    option_type: ForwardRef("OptionTypeEnum") = Field(None, description="The type of option transaction. From a usage standpoint, put/call is the default option type, while payer/receiver indicator is used for options on index credit default swaps, consistently with the industry practice. Straddle is used for the case of straddle strategy, that combine a call and a put with the same strike.")
    exercise_terms: ForwardRef("ExerciseTerms") = Field(description="The terms for exercising the option, which include the option style (e.g. American style option), the exercise procedure (e.g. manual exercise) and the settlement terms (e.g. physical vs. cash).")
    strike: ForwardRef("OptionStrike") = Field(None, description="Specifies the strike of the option")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.buyer_seller import BuyerSeller
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
from src.models.cdm.generated.product.common.schedule.observation_terms import ObservationTerms
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
from src.models.cdm.generated.product.template.option_feature import OptionFeature
from src.models.cdm.generated.product.template.option_strike import OptionStrike
from src.models.cdm.generated.product.template.option_type_enum import OptionTypeEnum
from src.models.cdm.generated.product.template.underlier import Underlier
OptionPayout.model_rebuild()
