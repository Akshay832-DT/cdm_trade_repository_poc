from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
    from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
    from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
    from src.models.cdm.generated.product.template.asset_leg import AssetLeg
    from src.models.cdm.generated.product.template.asset_payout_trade_type_enum import AssetPayoutTradeTypeEnum
    from src.models.cdm.generated.product.template.dividend_terms import DividendTerms

class AssetPayout(CdmModelBase):
    """Security finance payout specification in case the product payout involves some form of security collateral, as in a securities financing transaction. Plus additional description for ICMA."""
    payer_receiver: ForwardRef("PayerReceiver") = Field(None, description="Canonical representation of the payer and receiver parties applicable to each payout leg.")
    price_quantity: ForwardRef("ResolvablePriceQuantity") = Field(None, description="Each payout leg must implement the quantity concept as a 'resolvable' type, which allows for different payout legs to be linked to each other (e.g. in the case of cross-curreny products).")
    principal_payment: ForwardRef("PrincipalPayments") = Field(None, description="The specification of the principal exchange. Optional as only applicable in the case of cross-currency or zero-coupon swaps with a final payment.")
    settlement_terms: ForwardRef("SettlementTerms") = Field(None, description="Each payout leg must specifies its settlement terms, including the delivery type (i.e. cash vs physical, and their respective terms), the transfer type (DvP etc.) and settlement date, if any.")
    asset_leg: List[ForwardRef("AssetLeg")] = Field(None, description="Defines each asset movement as a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.")
    underlier: ForwardRef("Asset") = Field(description="Specifies the Purchased Asset, usually a Security.")
    minimum_fee: ForwardRef("Money") = Field(None, description="A contractual minimum amount which the borrower will pay, regardless of the duration of the loan. A mechanism for making sure that a trade generates enough income.")
    dividend_terms: ForwardRef("DividendTerms") = Field(None, description="Specifies the terms under which dividends received by the borrower are passed through to the lender.")
    trade_type: ForwardRef("AssetPayoutTradeTypeEnum") = Field(None, description="The trade type, eg repurchase transaction or buy/sell-back.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset import Asset
from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.common.settlement.principal_payments import PrincipalPayments
from src.models.cdm.generated.product.common.settlement.resolvable_price_quantity import ResolvablePriceQuantity
from src.models.cdm.generated.product.common.settlement.settlement_terms import SettlementTerms
from src.models.cdm.generated.product.template.asset_leg import AssetLeg
from src.models.cdm.generated.product.template.asset_payout_trade_type_enum import AssetPayoutTradeTypeEnum
from src.models.cdm.generated.product.template.dividend_terms import DividendTerms
AssetPayout.model_rebuild()
