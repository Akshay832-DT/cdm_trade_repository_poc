"""
FpML Trade Model
"""
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime
from ..base import FpMLTradeBase

# Define forward references for type checking only
PartyReferenceRef = ForwardRef('PartyReference')
PartyTradeIdentifierRef = ForwardRef('PartyTradeIdentifier')
TradeHeaderRef = ForwardRef('TradeHeader')
PayerReceiverRef = ForwardRef('PayerReceiver')
NotionalAmountRef = ForwardRef('NotionalAmount')
SwapStreamRef = ForwardRef('SwapStream')
InterestRateProductRef = ForwardRef('InterestRateProduct')
ProtectionTermsRef = ForwardRef('ProtectionTerms')
ReferenceInformationRef = ForwardRef('ReferenceInformation')
CreditProductRef = ForwardRef('CreditProduct')
ProductRef = ForwardRef('Product')

class PartyReference(FpMLTradeBase):
    """Reference to a party."""
    href: str = Field(alias="@href")

class PartyTradeIdentifier(FpMLTradeBase):
    """Trade identifier for a party."""
    partyReference: PartyReference
    tradeId: str
    
class TradeHeader(FpMLTradeBase):
    """Trade header information."""
    partyTradeIdentifier: List[PartyTradeIdentifier]
    tradeDate: date
    clearedDate: Optional[date] = None

class PayerReceiver(FpMLTradeBase):
    """Payer and receiver information."""
    payerPartyReference: PartyReference
    receiverPartyReference: PartyReference

class NotionalAmount(FpMLTradeBase):
    """Notional amount."""
    amount: float
    currency: str

class SwapStream(FpMLTradeBase):
    """Swap stream."""
    payerReceiver: PayerReceiver
    paymentFrequency: str
    notionalAmount: NotionalAmount

class InterestRateProduct(FpMLTradeBase):
    """Interest rate product."""
    swapStream: List[SwapStream]

class ProtectionTerms(FpMLTradeBase):
    """Credit derivative protection terms."""
    referenceEntity: str
    creditEvent: str
    settlementType: str

class ReferenceInformation(FpMLTradeBase):
    """Credit derivative reference information."""
    referenceEntity: str
    referenceObligation: Optional[str] = None

class CreditProduct(FpMLTradeBase):
    """Credit derivative product."""
    protectionTerms: ProtectionTerms
    referenceInformation: ReferenceInformation

class Product(FpMLTradeBase):
    """Trade product."""
    interestRate: Optional[InterestRateProduct] = None
    credit: Optional[CreditProduct] = None

class FpMLTrade(FpMLTradeBase):
    """FpML trade model."""
    tradeHeader: TradeHeader
    product: Product
    
    class Config:
        populate_by_field_name = True

# Update forward references
PartyReference.update_forward_refs()
PartyTradeIdentifier.update_forward_refs()
TradeHeader.update_forward_refs()
PayerReceiver.update_forward_refs()
NotionalAmount.update_forward_refs()
SwapStream.update_forward_refs()
InterestRateProduct.update_forward_refs()
ProtectionTerms.update_forward_refs()
ReferenceInformation.update_forward_refs()
CreditProduct.update_forward_refs()
Product.update_forward_refs()
FpMLTrade.update_forward_refs()
