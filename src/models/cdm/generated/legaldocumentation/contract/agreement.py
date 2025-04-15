from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.csa.collateral_transfer_agreement_elections import CollateralTransferAgreementElections
    from src.models.cdm.generated.legaldocumentation.csa.credit_support_agreement_elections import CreditSupportAgreementElections
    from src.models.cdm.generated.legaldocumentation.csa.security_agreement_elections import SecurityAgreementElections
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_schedule import MasterAgreementSchedule
    from src.models.cdm.generated.legaldocumentation.transaction.transaction_additional_terms import TransactionAdditionalTerms

class Agreement(CdmModelBase):
    """Specification of the standard set of terms that define a legal agreement."""
    credit_support_agreement_elections: ForwardRef("CreditSupportAgreementElections") = Field(None, description="Elections to specify a Credit Support Annex or Credit Support Deed for Intial or Variation Margin.")
    collateral_transfer_agreement_elections: ForwardRef("CollateralTransferAgreementElections") = Field(None, description="Elections to specify a Collateral Transfer Agreement.")
    security_agreement_elections: ForwardRef("SecurityAgreementElections") = Field(None, description="Elections to specify a Security agreement.")
    master_agreement_schedule: ForwardRef("MasterAgreementSchedule") = Field(None, description="Elections to specify a Master Agreement Schedule.")
    transaction_additional_terms: ForwardRef("TransactionAdditionalTerms") = Field(None, description="Any additional terms which mainly intend to specify the extraordinary events that may affect a trade and the related contractual rights and obligation of the parties when this happens")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.csa.collateral_transfer_agreement_elections import CollateralTransferAgreementElections
from src.models.cdm.generated.legaldocumentation.csa.credit_support_agreement_elections import CreditSupportAgreementElections
from src.models.cdm.generated.legaldocumentation.csa.security_agreement_elections import SecurityAgreementElections
from src.models.cdm.generated.legaldocumentation.master.master_agreement_schedule import MasterAgreementSchedule
from src.models.cdm.generated.legaldocumentation.transaction.transaction_additional_terms import TransactionAdditionalTerms
Agreement.model_rebuild()
