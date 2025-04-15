from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
    from src.models.cdm.generated.base.math.number_bound import NumberBound
    from src.models.cdm.generated.product.collateral.alternative_to_interest_amount_enum import AlternativeToInterestAmountEnum
    from src.models.cdm.generated.product.collateral.collateral_interest_handling_enum import CollateralInterestHandlingEnum
    from src.models.cdm.generated.product.collateral.collateral_interest_notification import CollateralInterestNotification
    from src.models.cdm.generated.product.collateral.interest_amount_application import InterestAmountApplication

class CollateralInterestHandlingParameters(CdmModelBase):
    """Represents parameters that describe how calculated interest amounts are handled, i.e. are they transferred/distributed, or is the collateral balance adjusted, is netting done, and any other special handling."""
    interest_payment_handling: ForwardRef("CollateralInterestHandlingEnum") = Field(description="Specifies how the collateral interest is to be handled.")
    payment_business_center: List[ForwardRef("BusinessCenterEnum")] = Field(None, description="Specifies applicable business centers for payments.")
    net_posted_and_held_interest: bool = Field(description="Indicates whether to net Held and Posted Interest Payments (i.e. whether interest payable for a period can be netted with interest receivable).")
    net_interest_with_margin_calls: bool = Field(description="Indicates whether the interest amount may be offset against any margin call deliver or return amounts?   (aka 'net payments' indicator).")
    include_accrual_in_margin_calc: bool = Field(description="Indicates whether or not to include the open interest accrual in the margin calculation.")
    accrue_interest_on_unsettled_interest: bool = Field(None, description="Indicates whether interest accruing on unsettled interest amount is included (continues to be accrued) in the following period.")
    on_full_return: bool = Field(description="Indicates the option that accrued interest should be calculated and distributed when a full return of collateral occurs.")
    on_partial_return: bool = Field(description="Indicates the option that accrued interest should be calculated and distributed when a partial return collateral occurs.")
    interest_amount_application: ForwardRef("InterestAmountApplication") = Field(None, description="The application of Interest Amount with respect to the Delivery Amount and the Return Amount.")
    interest_rollover_limit: ForwardRef("NumberBound") = Field(None, description="Specifies the level below which the interest will be rolled over.")
    writeoff_limit: ForwardRef("NumberBound") = Field(None, description="Specifies the level below which the interest will be written off; if omitted write-off is not applicable.")
    alternative_to_interest_amount: ForwardRef("AlternativeToInterestAmountEnum") = Field(None, description="Specifies the alternative to interest amounts.")
    alternative_provision: str = Field(None, description="Specifies an alternative to interest amount, when the alternative provision clause is specified.")
    cutoff_time: str = Field(None, description="Specifies the time of day that interest needs to be confirmed by.")
    notification: ForwardRef("CollateralInterestNotification") = Field(None, description="Specifies the terms describing notification requirements.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.business_center_enum import BusinessCenterEnum
from src.models.cdm.generated.base.math.number_bound import NumberBound
from src.models.cdm.generated.product.collateral.alternative_to_interest_amount_enum import AlternativeToInterestAmountEnum
from src.models.cdm.generated.product.collateral.collateral_interest_handling_enum import CollateralInterestHandlingEnum
from src.models.cdm.generated.product.collateral.collateral_interest_notification import CollateralInterestNotification
from src.models.cdm.generated.product.collateral.interest_amount_application import InterestAmountApplication
CollateralInterestHandlingParameters.model_rebuild()
