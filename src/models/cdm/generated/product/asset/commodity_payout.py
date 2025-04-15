from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
    from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.settlement.commodity_price_return_terms import CommodityPriceReturnTerms
    from src.models.cdm.generated.product.common.settlement.pricing_dates import PricingDates
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
    from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
    from src.models.cdm.generated.product.template.fx_feature import FxFeature
    from src.models.cdm.generated.product.template.underlier import Underlier

class CommodityPayout(CdmModelBase):
    """Payout based on the averaged price of a referenced underlier. (e.g. Commodities). Can represent both average (average of many) & bullet (average of 1) pricing"""
    payer_receiver: Optional[ForwardRef("PayerReceiver")] = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: Optional[ForwardRef("ResolvablePriceQuantity")] = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: Optional[ForwardRef("PrincipalPayments")] = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: Optional[ForwardRef("SettlementTerms")] = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    averaging_feature: Optional[ForwardRef("AveragingCalculation")] = Field(None, description="Indicates if the averaging calculation, when applicable, is weighted or unweighted.")
    commodity_price_return_terms: Optional[ForwardRef("CommodityPriceReturnTerms")] = Field(None, description="Defines parameters in which the commodity price is assessed.")
    pricing_dates: Optional[ForwardRef("PricingDates")] = Field(None, description="Specifies specific dates or parametric rules for the dates on which the price will be determined.")
    schedule: Optional[ForwardRef("CalculationSchedule")] = Field(None, description="Allows the full representation of a payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")
    calculation_period_dates: Optional[ForwardRef("CalculationPeriodDates")] = Field(None, description="Defines the calculation period dates schedule.")
    payment_dates: Optional[ForwardRef("PaymentDates")] = Field(None, description="Defines the payment date schedule, as defined by the parameters that are needed to specify it, either in a parametric way or by reference to another schedule of dates (e.g. the valuation dates).")
    underlier: Optional[ForwardRef("Underlier")] = Field(None, description="Identifies the underlying product that is referenced for pricing of the applicable leg in a swap. Referenced in the '2018 ISDA CDM Equity Confirmation for Security Equity Swap' as Security.")
    fx_feature: Optional[ForwardRef("FxFeature")] = Field(None, description="Defines quanto or composite FX features that are included in the swap leg.")
    delivery: Optional[ForwardRef("AssetDeliveryInformation")] = Field(None, description="Contains the information relative to the delivery of the asset.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
from src.models.cdm.generated.product.common.schedule.calculation_period_dates import CalculationPeriodDates
from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
from src.models.cdm.generated.product.common.settlement.commodity_price_return_terms import CommodityPriceReturnTerms
from src.models.cdm.generated.product.common.settlement.pricing_dates import PricingDates
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
from src.models.cdm.generated.product.template.fx_feature import FxFeature
from src.models.cdm.generated.product.template.underlier import Underlier
CommodityPayout.model_rebuild()
