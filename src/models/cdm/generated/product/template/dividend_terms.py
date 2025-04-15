from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.asset.dividend_entitlement_enum import DividendEntitlementEnum
    from src.models.cdm.generated.product.asset.dividend_payout_ratio import DividendPayoutRatio

class DividendTerms(CdmModelBase):
    """Information related to dividends and payments."""
    manufactured_income_requirement: ForwardRef("DividendPayoutRatio") = Field(description="Specifies the proportion of the value of the dividend on the borrowed shares that the borrower is legally obligated to return to the lender.")
    dividend_entitlement: ForwardRef("DividendEntitlementEnum") = Field(None, description="Defines the date on which the receiver of the equity return is entitled to the dividend.")
    minimum_billing_amount: ForwardRef("Money") = Field(None, description="daily fee increments accrue until a threshold is crossed, at which point payment becomes due)")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.asset.dividend_entitlement_enum import DividendEntitlementEnum
from src.models.cdm.generated.product.asset.dividend_payout_ratio import DividendPayoutRatio
DividendTerms.model_rebuild()
