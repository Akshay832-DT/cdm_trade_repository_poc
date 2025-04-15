"""
Test FpML model creation and validation.
"""
import unittest
from datetime import date
from src.models.fpml.generated.trade import FpMLTrade
from src.models.fpml.generated.common import (
    ProductType, TradeHeaderType, PartyTradeIdentifierType, 
    PartyReferenceType, InterestRateProductType, SwapStreamType,
    PayerReceiverType, NotionalAmountType
)
from src.models.fpml.generated.enums import PaymentFrequencyEnum, CurrencyEnum

class TestFpMLModels(unittest.TestCase):
    """Test for FpML model creation and validation."""
    
    def test_create_irs_model(self):
        """Test creating an interest rate swap model."""
        # Create a simple IRS model
        irs_trade = FpMLTrade(
            tradeHeader=dict(
                partyTradeIdentifier=[
                    dict(
                        partyReference=dict(**{"@href": "Party1"}),
                        tradeId="TRADE123"
                    ),
                    dict(
                        partyReference=dict(**{"@href": "Party2"}),
                        tradeId="TRADE456"
                    )
                ],
                tradeDate=date(2023, 4, 15)
            ),
            product=dict(
                interestRate=dict(
                    swapStream=[
                        dict(
                            payerReceiver=dict(
                                payerPartyReference=dict(**{"@href": "Party1"}),
                                receiverPartyReference=dict(**{"@href": "Party2"})
                            ),
                            paymentFrequency=PaymentFrequencyEnum.Quarterly,
                            notionalAmount=dict(
                                amount=1000000,
                                currency=CurrencyEnum.USD
                            )
                        )
                    ]
                )
            )
        )
        
        # Validate the model
        self.assertEqual(irs_trade.tradeHeader.partyTradeIdentifier[0].partyReference.href, "Party1")
        self.assertEqual(irs_trade.tradeHeader.partyTradeIdentifier[0].tradeId, "TRADE123")
        self.assertEqual(irs_trade.tradeHeader.tradeDate, date(2023, 4, 15))
        self.assertEqual(irs_trade.product.interestRate.swapStream[0].paymentFrequency, PaymentFrequencyEnum.Quarterly)
        self.assertEqual(irs_trade.product.interestRate.swapStream[0].notionalAmount.amount, 1000000)
        self.assertEqual(irs_trade.product.interestRate.swapStream[0].notionalAmount.currency, CurrencyEnum.USD)

    def test_create_product_type_directly(self):
        """Test creating a product type directly to verify circular dependencies."""
        product = ProductType(
            interestRate=InterestRateProductType(
                swapStream=[
                    SwapStreamType(
                        payerReceiver=PayerReceiverType(
                            payerPartyReference=PartyReferenceType(**{"@href": "Party1"}),
                            receiverPartyReference=PartyReferenceType(**{"@href": "Party2"})
                        ),
                        paymentFrequency=PaymentFrequencyEnum.Monthly,
                        notionalAmount=NotionalAmountType(
                            amount=500000,
                            currency=CurrencyEnum.EUR
                        )
                    )
                ]
            )
        )
        
        # Validate the model
        self.assertEqual(product.interestRate.swapStream[0].payerReceiver.payerPartyReference.href, "Party1")
        self.assertEqual(product.interestRate.swapStream[0].paymentFrequency, PaymentFrequencyEnum.Monthly)
        self.assertEqual(product.interestRate.swapStream[0].notionalAmount.currency, CurrencyEnum.EUR)

if __name__ == '__main__':
    unittest.main() 