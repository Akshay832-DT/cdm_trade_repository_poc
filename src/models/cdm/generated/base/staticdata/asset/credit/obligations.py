from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
    from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
    from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class Obligations(CdmModelBase):
    """A class to specify the underlying obligations of the reference entity on which protection is purchased or sold through the Credit Default Swap."""
    category: ForwardRef("ObligationCategoryEnum") = Field(description="Used in both obligations and deliverable obligations to represent a class or type of securities which apply. ISDA 2003 Term: Obligation Category/Deliverable Obligation Category.")
    not_subordinated: bool = Field(None, description="An obligation and deliverable obligation characteristic. An obligation that ranks at least equal with the most senior Reference Obligation in priority of payment or, if no Reference Obligation is specified in the related Confirmation, the obligations of the Reference Entity that are senior. ISDA 2003 Term: Not Subordinated.")
    specified_currency: ForwardRef("SpecifiedCurrency") = Field(None, description="An obligation and deliverable obligation characteristic. The currency or currencies in which an obligation or deliverable obligation must be payable. ISDA 2003 Term: Specified Currency.")
    not_sovereign_lender: bool = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation that is not primarily (majority) owed to a Sovereign or Supranational Organisation. ISDA 2003 Term: Not Sovereign Lender.")
    not_domestic_currency: ForwardRef("NotDomesticCurrency") = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation that is payable in any currency other than the domestic currency. Domestic currency is either the currency so specified or, if no currency is specified, the currency of (a) the reference entity, if the reference entity is a sovereign, or (b) the jurisdiction in which the relevant reference entity is organised, if the reference entity is not a sovereign. ISDA 2003 Term: Not Domestic Currency.")
    not_domestic_law: bool = Field(None, description="An obligation and deliverable obligation characteristic. If the reference entity is a Sovereign, this means any obligation that is not subject to the laws of the reference entity. If the reference entity is not a sovereign, this means any obligation that is not subject to the laws of the jurisdiction of the reference entity. ISDA 2003 Term: Not Domestic Law.")
    listed: bool = Field(None, description="An obligation and deliverable obligation characteristic. Indicates whether or not the obligation is quoted, listed or ordinarily purchased and sold on an exchange. ISDA 2003 Term: Listed.")
    not_domestic_issuance: bool = Field(None, description="An obligation and deliverable obligation characteristic. Any obligation other than an obligation that was intended to be offered for sale primarily in the domestic market of the relevant Reference Entity. This specifies that the obligation must be an internationally recognised bond. ISDA 2003 Term: Not Domestic Issuance.")
    full_faith_and_credit_ob_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: Full Faith and Credit Obligation Liability.")
    general_fund_obligation_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: General Fund Obligation Liability.")
    revenue_obligation_liability: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published additional provisions for U.S. Municipal as Reference Entity. ISDA 2003 Term: Revenue Obligation Liability.")
    not_contingent: bool = Field(None, description="OTE: Only allowed as an obligation characteristic under ISDA Credit 1999. In essence Not Contingent means the repayment of principal cannot be dependent on a formula/index, i.e. to prevent the risk of being delivered an instrument that may never pay any element of principal, and to ensure that the obligation is interest bearing (on a regular schedule). ISDA 2003 Term: Not Contingent.")
    excluded: str = Field(None, description="A free format string to specify any excluded obligations or deliverable obligations, as the case may be, of the reference entity or excluded types of obligations or deliverable obligations. ISDA 2003 Term: Excluded Obligations/Excluded Deliverable Obligations.")
    oth_reference_entity_obligations: str = Field(None, description="This element is used to specify any other obligations of a reference entity in both obligations and deliverable obligations. The obligations can be specified free-form. ISDA 2003 Term: Other Obligations of a Reference Entity.")
    designated_priority: ForwardRef("FieldWithMetaString") = Field(None, description="Applies to Loan CDS, to indicate what lien level is appropriate for a deliverable obligation. Applies to European Loan CDS, to indicate the Ranking of the obligation. Example: a 2nd lien Loan CDS would imply that the deliverable obligations are 1st or 2nd lien loans.")
    cash_settlement_only: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published Standard Terms Supplement for use with CDS Transactions on Leveraged Loans. ISDA 2003 Term: Cash Settlement Only.")
    delivery_of_commitments: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published Standard Terms Supplement for use with CDS Transactions on Leveraged Loans. ISDA 2003 Term: Delivery of Commitments.")
    continuity: bool = Field(None, description="An obligation and deliverable obligation characteristic. Defined in the ISDA published Standard Terms Supplement for use with CDS Transactions on Leveraged Loans. ISDA 2003 Term: Continuity.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
Obligations.model_rebuild()
