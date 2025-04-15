"""
Generated FpML model classes.
"""
# Import base classes first to avoid circular imports
from .base.base import FpMLModelBase, FpMLTradeBase, FpMLComponentBase, FpMLMessageBase

# Import enums (these have no dependencies)
from .enums.payment_frequency_enum import PaymentFrequencyEnum
from .enums.currency_enum import CurrencyEnum
from .enums.credit_event_enum import CreditEventEnum
from .enums.settlement_type_enum import SettlementTypeEnum

# Import common types in dependency order
from .common.party_reference_type import PartyReferenceType
from .common.party_trade_identifier_type import PartyTradeIdentifierType
from .common.trade_header_type import TradeHeaderType
from .common.payer_receiver_type import PayerReceiverType
from .common.notional_amount_type import NotionalAmountType
from .common.swap_stream_type import SwapStreamType
from .common.interest_rate_product_type import InterestRateProductType
from .common.protection_terms_type import ProtectionTermsType
from .common.reference_information_type import ReferenceInformationType
from .common.credit_product_type import CreditProductType
from .common.product_type import ProductType
from .common.trade_type import TradeType
from .common.fp_ml_type import FpMLType

# Import trade models 
from .trade.trade import (
    PartyReference, PartyTradeIdentifier, TradeHeader, 
    PayerReceiver, NotionalAmount, SwapStream, 
    InterestRateProduct, ProtectionTerms, ReferenceInformation,
    CreditProduct, Product, FpMLTrade
)

__all__ = [
    "FpMLModelBase",
    "FpMLTradeBase", 
    "FpMLComponentBase",
    "FpMLMessageBase",
    "FpMLTrade",
    
    # Enums
    "PaymentFrequencyEnum",
    "CurrencyEnum",
    "CreditEventEnum",
    "SettlementTypeEnum",
    
    # Common types
    "PartyReferenceType",
    "PartyTradeIdentifierType",
    "TradeHeaderType",
    "PayerReceiverType",
    "NotionalAmountType",
    "SwapStreamType",
    "InterestRateProductType",
    "ProtectionTermsType",
    "ReferenceInformationType",
    "CreditProductType",
    "ProductType",
    "TradeType",
    "FpMLType",
    
    # Trade components
    "PartyReference",
    "PartyTradeIdentifier",
    "TradeHeader",
    "PayerReceiver",
    "NotionalAmount", 
    "SwapStream",
    "InterestRateProduct",
    "ProtectionTerms",
    "ReferenceInformation",
    "CreditProduct",
    "Product"
]
