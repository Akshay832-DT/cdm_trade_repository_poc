from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
    from src.models.cdm.generated.product.common.settlement.fixed_price import FixedPrice
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule

class FixedPricePayout(CdmModelBase):
    """Represents a fixed price payout. There is no underlier associated with this payout type and is based on fixed pricing per a given unit (e.g. in commodities price per barrel)"""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    payment_dates: ForwardRef("PaymentDates") = Field(description="Specifies the parameters to generate the payment date schedule, either through a parametric representation or by reference to specified dates.")
    fixed_price: ForwardRef("FixedPrice") = Field(description="Specifies the fixed price on which fixed forward payments are based.")
    schedule: ForwardRef("CalculationSchedule") = Field(None, description="Allows the full representation of a payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.product.common.schedule.payment_dates import PaymentDates
from src.models.cdm.generated.product.common.settlement.fixed_price import FixedPrice
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
FixedPricePayout.model_rebuild()
