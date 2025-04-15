from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.period import Period
    from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
    from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
    from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
    from src.models.cdm.generated.product.common.settlement.loan_participation import LoanParticipation
    from src.models.cdm.generated.product.common.settlement.pc_deliverable_obligation_charac import PCDeliverableObligationCharac

class DeliverableObligations(CdmModelBase):
    """A class to specify all the ISDA terms relevant to defining the deliverable obligations."""
    accrued_interest: bool = Field(None, description="Indicates whether accrued interest is included (true) or not (false). For cash settlement this specifies whether quotations should be obtained inclusive or not of accrued interest. For physical settlement this specifies whether the buyer should deliver the obligation with an outstanding principal balance that includes or excludes accrued interest. ISDA 2003 Term: Include/Exclude Accrued Interest.")
    category: ForwardRef("ObligationCategoryEnum") = Field(None, description="Used in both obligations and deliverable obligations to represent a class or type of securities which apply. ISDA 2003 Term: Obligation Category/Deliverable Obligation Category.")
    not_subordinated: bool = Field(None, description="An obligation and deliverable obligation characteristic. An obligation that ranks at least equal with the most senior Reference Obligation in priority of payment or, if no Reference Obligation is specified in the related Confirmation, the obligations of the Reference Entity that are senior. ISDA 2003 Term: Not Subordinated.")
    specified_currency: ForwardRef("SpecifiedCurrency") = Field(None, description="An obligation and deliverable obligation characteristic. The currency or currencies in which an obligation or deliverable obligation must be payable. ISDA 2003 Term: Specified Currency.")
    not_sovereign_lender: bool = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation that is not primarily (majority) owed to a Sovereign or Supranational Organisation. ISDA 2003 Term: Not Sovereign Lender.")
    not_domestic_currency: ForwardRef("NotDomesticCurrency") = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation that is payable in any currency other than the domestic currency. Domestic currency is either the currency so specified or, if no currency is specified, the currency of (a) the reference entity, if the reference entity is a sovereign, or (b) the jurisdiction in which the relevant reference entity is organised, if the reference entity is not a sovereign. ISDA 2003 Term: Not Domestic Currency.")
    not_domestic_law: bool = Field(None, description="An obligation and deliverable obligation characteristic. If the reference entity is a Sovereign, this means any obligation that is not subject to the laws of the reference entity. If the reference entity is not a sovereign, this means any obligation that is not subject to the laws of the jurisdiction of the reference entity. ISDA 2003 Term: Not Domestic Law.")
    listed: bool = Field(None, description="An obligation and deliverable obligation characteristic. Indicates whether or not the obligation is quoted, listed or ordinarily purchased and sold on an exchange. ISDA 2003 Term: Listed.")
    not_contingent: bool = Field(None, description="A deliverable obligation characteristic. In essence Not Contingent means the repayment of principal cannot be dependant on a formula/index, i.e. to prevent the risk of being delivered an instrument that may never pay any element of principal, and to ensure that the obligation is interest bearing (on a regular schedule). ISDA 2003 Term: Not Contingent.")
    not_domestic_issuance: bool = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation other than an obligation that was intended to be offered for sale primarily in the domestic market of the relevant Reference Entity. This specifies that the obligation must be an internationally recognised bond. ISDA 2003 Term: Not Domestic Issuance.")
    assignable_loan: ForwardRef("PCDeliverableObligationCharac") = Field(None, description="A deliverable obligation characteristic. A loan that is freely assignable to a bank or financial institution without the consent of the Reference Entity or the guarantor, if any, of the loan (or the consent of the applicable borrower if a Reference Entity is guaranteeing the loan) or any agent. ISDA 2003 Term: Assignable Loan.")
    consent_required_loan: ForwardRef("PCDeliverableObligationCharac") = Field(None, description="A deliverable obligation characteristic. A loan that is capable of being assigned with the consent of the Reference Entity or the guarantor, if any, of the loan or any agent. ISDA 2003 Term: Consent Required Loan.")
    direct_loan_participation: ForwardRef("LoanParticipation") = Field(None, description="A deliverable obligation characteristic. A loan with a participation agreement whereby the buyer is capable of creating, or procuring the creation of, a contractual right in favour of the seller that provides the seller with recourse to the participation seller for a specified share in any payments due under the relevant loan which are received by the participation seller. ISDA 2003 Term: Direct Loan Participation.")
    transferable: bool = Field(None, description="A deliverable obligation characteristic. An obligation that is transferable to institutional investors without any contractual, statutory or regulatory restrictions. ISDA 2003 Term: Transferable.")
    maximum_maturity: ForwardRef("Period") = Field(None, description="A deliverable obligation characteristic. An obligation that has a remaining maturity from the Physical Settlement Date of not greater than the period specified. ISDA 2003 Term: Maximum Maturity.")
    accelerated_or_matured: bool = Field(None, description="A deliverable obligation characteristic. An obligation at time of default is due to mature and due to be repaid, or as a result of downgrade/bankruptcy is due to be repaid as a result of an acceleration clause. ISDA 2003 Term: Accelerated or Matured.")
    not_bearer: bool = Field(None, description="A deliverable obligation characteristic. Any obligation that is not a bearer instrument. This applies to Bonds only and is meant to avoid tax, fraud and security/delivery provisions that can potentially be associated with Bearer Bonds. ISDA 2003 Term: Not Bearer.")
    full_faith_and_credit_ob_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: Full Faith and Credit Obligation Liability.")
    general_fund_obligation_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: General Fund Obligation Liability.")
    revenue_obligation_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: Revenue Obligation Liability.")
    indirect_loan_participation: ForwardRef("LoanParticipation") = Field(None, description="ISDA 1999 Term: Indirect Loan Participation. NOTE: Only applicable as a deliverable obligation under ISDA Credit 1999.")
    excluded: str = Field(None, description="A free format string to specify any excluded obligations or deliverable obligations, as the case may be, of the reference entity or excluded types of obligations or deliverable obligations. ISDA 2003 Term: Excluded Obligations/Excluded Deliverable Obligations.")
    oth_reference_entity_obligations: str = Field(None, description="This element is used to specify any other obligations of a reference entity in both obligations and deliverable obligations. The obligations can be specified free-form. ISDA 2003 Term: Other Obligations of a Reference Entity.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.period import Period
from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
from src.models.cdm.generated.product.common.settlement.loan_participation import LoanParticipation
from src.models.cdm.generated.product.common.settlement.pc_deliverable_obligation_charac import PCDeliverableObligationCharac
DeliverableObligations.model_rebuild()
