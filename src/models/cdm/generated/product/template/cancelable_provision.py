from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
    from src.models.cdm.generated.base.datetime.adjustable_or_relative_dates import AdjustableOrRelativeDates
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.event.common.transfer import Transfer
    from src.models.cdm.generated.product.common.schedule.final_calculation_period_date_adjustment import FinalCalculationPeriodDateAdjustment
    from src.models.cdm.generated.product.template.calling_party_enum import CallingPartyEnum
    from src.models.cdm.generated.product.template.cancelable_provision_adjusted_dates import CancelableProvisionAdjustedDates
    from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
    from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms

class CancelableProvision(CdmModelBase):
    """A data defining:  the right of a party to cancel a swap transaction on the specified exercise dates. The provision is for 'walk-away' cancellation (i.e. the fair value of the swap is not paid). A fee payable on exercise can be specified. As a difference from the FpML construct, the canonical model extends the BuyerSeller class."""
    buyer: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Buyer party that can be resolved as one of the two principal parties to the transaction. The party that buys this instrument, i.e. pays for this instrument and receives the rights defined by it. ISDA 2002 Equity Definitions section 1.18: `Buyer` means the party specified as such in the related Confirmation. | ISDA 2006 Definitions article 12.1 (b)(i) relating to a Swaption: 'Buyer' means the party that will, on each Premium Payment Date, pay to Seller the Premium | ISDA 2006 Definitions article 12.1 (b)(ii) relating to Swap Transactions with applicable Early Termination: the party specified as such in the related Confirmation, or the Exercising Party if neither party is specified | ISDA 2006 Definitions article 12.1 (b)(iii) relating to any other Option Transaction: the party specified as such in the related Confirmation. | ISDA 2014 Credit Definition article 1.4: `Buyer` means the Fixed Rate Payer.")
    seller: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Seller party that can be resolved as one of the two principal parties to the transaction. The party that sells ('writes') this instrument, i.e. that grants the rights defined by this instrument and in return receives a payment for it. ISDA 2002 Equity Definitions section 1.19: `Seller` means the party specified as such in the related Confirmation. | ISDA 2006 Definitions article 12.1 (a)(i) relating to a Swaption: 'Seller' means the party the party specified as such or as writer in the related Confirmation | ISDA 2006 Definitions article 12.1 (a)(ii) relating to Swap Transactions with applicable Early Termination: the party specified as such or as writer in the related Confirmation or, if neither party is specified as such, the Non-exercising Party | ISDA 2006 Definitions article 12.1 (a)(iii) relating to any other Option Transaction: the party specified as such in the related Confirmation. | ISDA 2014 Credit Definition article 1.4: `Seller` means the Floating Rate Payer.")
    exercise_notice: ForwardRef("ExerciseNotice") = Field(None, description="Definition of the party to whom notice of exercise should be given.")
    follow_up_confirmation: bool = Field(description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
    cancelable_provision_adjusted_dates: ForwardRef("CancelableProvisionAdjustedDates") = Field(None, description="The adjusted dates associated with a cancelable provision. These dates have been adjusted for any applicable business day convention.")
    final_calculation_period_date_adjustment: List[ForwardRef("FinalCalculationPeriodDateAdjustment")] = Field(None, description="Business date convention adjustment to final payment period per leg (swapStream) upon exercise event. The adjustments can be made in-line with leg level BDC's or they can be specified separately.")
    initial_fee: ForwardRef("Transfer") = Field(None, description="An initial fee for the cancelable option.")
    calling_party: ForwardRef("CallingPartyEnum") = Field(None, description="The party with right to exercise a cancellation. Allows for buyer, seller or either.")
    earliest_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The first day when cancelation is permitted to take effect. A party may give notice prior to this date and taken together with the effective period would be necessary to cancel on this date.")
    expiration_date: ForwardRef("AdjustableOrRelativeDate") = Field(None, description="The last day within the term of the contract that cancelation is allowed.")
    effective_date: ForwardRef("AdjustableOrRelativeDates") = Field(None, description="The effective date if cancelation is invoked otherwise the cancellation period defines the cancellation date.")
    effective_period: ForwardRef("Period") = Field(None, description="Effective period for cancelation when notice is given. This is the period after notice is given that cancellation becomes effecticve.")
    earliest_cancellation_time: ForwardRef("BusinessCenterTime") = Field(None, description="The earliest time in a business day that notice of cancelation can be given.")
    latest_cancelation_time: ForwardRef("BusinessCenterTime") = Field(None, description="The latest time at which notice of cancelation can be given.")
    exercise_terms: ForwardRef("ExerciseTerms") = Field(description="The exercise terms associated with the cancelable provision, including details such as exercise style, exercise fees, and any other relevant conditions or terms governing the cancellation of the swap transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_relative_date import AdjustableOrRelativeDate
from src.models.cdm.generated.base.datetime.adjustable_or_relative_dates import AdjustableOrRelativeDates
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.event.common.transfer import Transfer
from src.models.cdm.generated.product.common.schedule.final_calculation_period_date_adjustment import FinalCalculationPeriodDateAdjustment
from src.models.cdm.generated.product.template.calling_party_enum import CallingPartyEnum
from src.models.cdm.generated.product.template.cancelable_provision_adjusted_dates import CancelableProvisionAdjustedDates
from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
CancelableProvision.model_rebuild()
