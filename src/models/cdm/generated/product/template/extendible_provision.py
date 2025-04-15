from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
    from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.product.template.calling_party_enum import CallingPartyEnum
    from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
    from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
    from src.models.cdm.generated.product.template.extendible_provision_adjusted_dates import ExtendibleProvisionAdjustedDates

class ExtendibleProvision(CdmModelBase):
    """A data defining:  an option to extend an existing swap transaction on the specified exercise dates for a term ending on the specified new termination date. As a difference from FpML, it extends the BuyerSeller class, which represents the BuyerSeller.model."""
    buyer: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Buyer party that can be resolved as one of the two principal parties to the transaction. The party that buys this instrument, i.e. pays for this instrument and receives the rights defined by it. ISDA 2002 Equity Definitions section 1.18: `Buyer` means the party specified as such in the related Confirmation. | ISDA 2006 Definitions article 12.1 (b)(i) relating to a Swaption: 'Buyer' means the party that will, on each Premium Payment Date, pay to Seller the Premium | ISDA 2006 Definitions article 12.1 (b)(ii) relating to Swap Transactions with applicable Early Termination: the party specified as such in the related Confirmation, or the Exercising Party if neither party is specified | ISDA 2006 Definitions article 12.1 (b)(iii) relating to any other Option Transaction: the party specified as such in the related Confirmation. | ISDA 2014 Credit Definition article 1.4: `Buyer` means the Fixed Rate Payer.")
    seller: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Seller party that can be resolved as one of the two principal parties to the transaction. The party that sells ('writes') this instrument, i.e. that grants the rights defined by this instrument and in return receives a payment for it. ISDA 2002 Equity Definitions section 1.19: `Seller` means the party specified as such in the related Confirmation. | ISDA 2006 Definitions article 12.1 (a)(i) relating to a Swaption: 'Seller' means the party the party specified as such or as writer in the related Confirmation | ISDA 2006 Definitions article 12.1 (a)(ii) relating to Swap Transactions with applicable Early Termination: the party specified as such or as writer in the related Confirmation or, if neither party is specified as such, the Non-exercising Party | ISDA 2006 Definitions article 12.1 (a)(iii) relating to any other Option Transaction: the party specified as such in the related Confirmation. | ISDA 2014 Credit Definition article 1.4: `Seller` means the Floating Rate Payer.")
    exercise_notice: ForwardRef("ExerciseNotice") = Field(None, description="Definition of the party to whom notice of exercise should be given.")
    follow_up_confirmation: bool = Field(None, description="A flag to indicate whether follow-up confirmation of exercise (written or electronic) is required following telephonic notice by the buyer to the seller or seller's agent.")
    extendible_provision_adjusted_dates: ForwardRef("ExtendibleProvisionAdjustedDates") = Field(None, description="The adjusted dates associated with an extendible provision. These dates have been adjusted for any applicable business day convention.")
    calling_party: ForwardRef("CallingPartyEnum") = Field(None)
    single_party_option: ForwardRef("PartyRole") = Field(None, description="If the ability to extend the contract is not available to both parties then this component specifies the buyer and seller of the option.")
    notice_deadline_period: ForwardRef("RelativeDateOffset") = Field(None, description="Defines the minimum period before a contract is scheduled to terminate that notice can be given that it will terminate beyond the scheduled termination date.")
    notice_deadline_date_time: str = Field(None, description="A specific date and time for the notice deadline")
    extension_term: ForwardRef("RelativeDateOffset") = Field(None, description="The length of each extension period relative to the effective date of the preceding contract.")
    extension_period: ForwardRef("AdjustableRelativeOrPeriodicDates") = Field(None, description="The period within which notice can be given that the contract will be extended.")
    exercise_terms: ForwardRef("ExerciseTerms") = Field(description="The exercise terms associated with the extendible provision, including details such as exercise style, exercise fees, and any other relevant conditions or terms governing the extension of the swap transaction.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_relative_or_periodic_dates import AdjustableRelativeOrPeriodicDates
from src.models.cdm.generated.base.datetime.relative_date_offset import RelativeDateOffset
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.product.template.calling_party_enum import CallingPartyEnum
from src.models.cdm.generated.product.template.exercise_notice import ExerciseNotice
from src.models.cdm.generated.product.template.exercise_terms import ExerciseTerms
from src.models.cdm.generated.product.template.extendible_provision_adjusted_dates import ExtendibleProvisionAdjustedDates
ExtendibleProvision.model_rebuild()
