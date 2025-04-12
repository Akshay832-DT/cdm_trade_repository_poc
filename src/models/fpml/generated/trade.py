from pydantic import BaseModel, Field
from typing import Dict, Optional, List
from datetime import datetime
from ..base import TradeModel

class PartyTradeIdentifier(BaseModel):
    partyReference: str
    tradeId: str

class TradeHeader(BaseModel):
    partyTradeIdentifier: List[PartyTradeIdentifier]
    tradeDate: datetime
    clearedDate: Optional[datetime] = None

class SwapStream(BaseModel):
    payerPartyReference: str
    receiverPartyReference: str
    paymentFrequency: str
    notional: float
    currency: str

class InterestRateProduct(BaseModel):
    swapStream: List[SwapStream]

class ProtectionTerms(BaseModel):
    referenceEntity: str
    creditEvent: str
    settlementType: str

class ReferenceInformation(BaseModel):
    referenceEntity: str
    referenceObligation: Optional[str] = None

class CreditProduct(BaseModel):
    protectionTerms: ProtectionTerms
    referenceInformation: ReferenceInformation

class Product(BaseModel):
    interestRate: Optional[InterestRateProduct] = None
    credit: Optional[CreditProduct] = None

class FpMLTrade(TradeModel):
    tradeHeader: TradeHeader
    product: Product

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        } 