from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.agreement_name import AgreementName
    from src.models.cdm.generated.legaldocumentation.common.governing_law_enum import GoverningLawEnum
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_publisher_enum import LegalAgreementPublisherEnum

class LegalAgreementIdentification(CdmModelBase):
    """Specifies the type of legal agreement, identified via a set of composable attributes: agreementName, publisher, governing law and version, e.g. ISDA 2013 Standard Credit Support Annex English Law."""
    governing_law: ForwardRef("GoverningLawEnum") = Field(None, description="The law governing the legal agreement, e.g. English Law, New York Law or Japanese Law.")
    agreement_name: ForwardRef("AgreementName") = Field(description="The legal agreement name, e.g. Credit Support Annex for Variation Margin.")
    publisher: ForwardRef("LegalAgreementPublisherEnum") = Field(None, description="The legal agreement publisher, e.g. ISDA.")
    vintage: int = Field(None, description="In the case where successive definitions of the legal agreement have been developed, the vintage identification. This is typically (but not necessarily) done by referencing the year, e.g. 2013 in the case of the ISDA 2013 Standard Credit Support Annex.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.agreement_name import AgreementName
from src.models.cdm.generated.legaldocumentation.common.governing_law_enum import GoverningLawEnum
from src.models.cdm.generated.legaldocumentation.common.legal_agreement_publisher_enum import LegalAgreementPublisherEnum
LegalAgreementIdentification.model_rebuild()
