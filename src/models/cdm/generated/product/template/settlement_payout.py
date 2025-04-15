from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
    from src.models.cdm.generated.product.template.underlier import Underlier

class SettlementPayout(CdmModelBase):
    """Represents a forward settling payout. The underlier attribute captures the underlying payout, which is settled according to the settlementTerms attribute (which is part of PayoutBase). Both FX Spot and FX Forward should use this component."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    underlier: ForwardRef("Underlier") = Field(description="The underlying financial product that will be physically or cash settled, which can be of any type, eg an asset such as cash or a security, or the cash settlement of an index rate.")
    delivery_term: str = Field(None, description="Also called contract month or delivery month. However, it's not always a month. It is usually expressed using a code, e.g. Z23 would be the Dec 2023 contract, (Z = December). For crude oil, the corresponding contract might be called CLZ23.")
    delivery: ForwardRef("AssetDeliveryInformation") = Field(None, description="Contains the information relative to the delivery of the asset.")
    schedule: ForwardRef("CalculationSchedule") = Field(None, description="Allows the full representation of a payout by defining a set of schedule periods. It supports standard schedule customization by expressing all the dates, quantities, and pricing data in a non-parametric way.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.product.asset.asset_delivery_information import AssetDeliveryInformation
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.calculation_schedule import CalculationSchedule
from src.models.cdm.generated.product.template.underlier import Underlier
SettlementPayout.model_rebuild()
