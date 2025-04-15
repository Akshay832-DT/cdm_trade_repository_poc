"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.csa.collateral_transfer_agreement_elections import CollateralTransferAgreementElections
    from src.models.cdm.generated.legaldocumentation.csa.credit_support_agreement_elections import CreditSupportAgreementElections
    from src.models.cdm.generated.legaldocumentation.csa.security_agreement_elections import SecurityAgreementElections
