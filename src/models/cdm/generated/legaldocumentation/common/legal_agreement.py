from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.legaldocumentation.common.agreement_terms import AgreementTerms
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_identification import LegalAgreementIdentification
    from src.models.cdm.generated.legaldocumentation.common.resource import Resource
    from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement import UmbrellaAgreement
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class LegalAgreement(CdmModelBase):
    """The specification of a legal agreement between two parties, being negotiated or having been executed. This includes the baseline information and the optional specialised elections"""
    agreement_date: str = Field(None, description="The date on which the legal agreement has been agreed between the parties. This corresponds to the Date of Deed in an English Law document.")
    effective_date: str = Field(None, description="The date on which, or as of which, the agreement is effective, if different from the agreement date. It is expected that it will most often correspond to the agreement date, although there could be situations where the parties will explicitly agree on a distinct effective date.")
    identifier: List[ForwardRef("Identifier")] = Field(None, description="The legal agreement identifier. Several identifiers can be specified.")
    legal_agreement_identification: ForwardRef("LegalAgreementIdentification") = Field(None, description="The type of legal agreement, identified via a set of composable attributes: agreementName, publisher, governing law and version, e.g. ISDA 2013 Standard Credit Support Annex English Law.")
    contractual_party: List[ForwardRef("ReferenceWithMetaParty")] = Field(None, description="The two contractual parties to the legal agreement, which reference information is positioned as part of the partyInformation attribute.")
    other_party: List[ForwardRef("PartyRole")] = Field(None, description="The role(s) that other party(ies) may have in relation to the legal agreement, further to the contractual parties.")
    attachment: List[ForwardRef("Resource")] = Field(None, description="A human readable document, for example a confirmation.")
    agreement_terms: ForwardRef("AgreementTerms") = Field(None, description="Specification of the content of the legal agreement.")
    related_agreements: List[ForwardRef("LegalAgreement")] = Field(None, description="Specifies the agreement(s) that govern the agreement, either as a reference to such agreements when specified as part of the CDM, or through identification of some of the key terms of those agreements, such as the type of agreement, the publisher, the vintage, the agreement identifier and the agreement date.")
    umbrella_agreement: ForwardRef("UmbrellaAgreement") = Field(None, description="The determination of whether Umbrella Agreement terms are applicable (True) or Not Applicable (False).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.legaldocumentation.common.agreement_terms import AgreementTerms
from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
from src.models.cdm.generated.legaldocumentation.common.legal_agreement_identification import LegalAgreementIdentification
from src.models.cdm.generated.legaldocumentation.common.resource import Resource
from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement import UmbrellaAgreement
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
LegalAgreement.model_rebuild()
