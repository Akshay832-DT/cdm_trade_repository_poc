"""
FpML Complex Type - SwapStreamType
"""

from typing import List, Optional, Any, Dict, ForwardRef, TYPE_CHECKING
from pydantic import Field
from datetime import date, datetime, time
from ..base import FpMLModelBase

# Import directly for use at runtime
from .notional_amount_type import NotionalAmountType
from .payer_receiver_type import PayerReceiverType

# Only use the forward references for type checking
NotionalAmountTypeRef = ForwardRef('NotionalAmountType')
PayerReceiverTypeRef = ForwardRef('PayerReceiverType')

from ..enums.payment_frequency_enum import PaymentFrequencyEnum

class SwapStreamType(FpMLModelBase):
    class Config:
        populate_by_field_name = True
        validate_assignment = True

    payerReceiver: PayerReceiverType = Field()
    paymentFrequency: PaymentFrequencyEnum = Field()
    notionalAmount: NotionalAmountType = Field()

# Update forward references
SwapStreamType.update_forward_refs()
