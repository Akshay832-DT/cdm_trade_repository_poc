from pydantic import BaseModel, Field
from typing import Dict, Optional, List
from datetime import datetime
from ..base import TradeModel

class TradeIdentifier(BaseModel):
    tradeId: str
    source: str

class TradeHeader(BaseModel):
    tradeIdentifier: List[TradeIdentifier]
    tradeDate: datetime
    tradeTime: Optional[datetime] = None

class SwapStream(BaseModel):
    payerPartyReference: str
    receiverPartyReference: str
    paymentFrequency: str
    notional: float
    currency: str
    fixedRate: Optional[float] = None
    floatingRateIndex: Optional[str] = None

class InterestRateProduct(BaseModel):
    swapStream: List[SwapStream]

class ProtectionTerms(BaseModel):
    referenceEntity: str
    creditEvent: List[str]
    settlementType: str
    paymentFrequency: str
    notional: float
    currency: str

class ReferenceInformation(BaseModel):
    referenceEntity: str
    referenceObligation: Optional[str] = None
    referencePrice: Optional[float] = None

class CreditProduct(BaseModel):
    protectionTerms: ProtectionTerms
    referenceInformation: ReferenceInformation

class Product(BaseModel):
    interestRate: Optional[InterestRateProduct] = None
    credit: Optional[CreditProduct] = None

class CDMTrade(TradeModel):
    tradeHeader: TradeHeader
    product: Product

    class Config:
        allow_population_by_field_name = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        } 