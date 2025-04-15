from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
    from src.models.cdm.generated.metafields.field_with_meta_governing_law_enum import FieldWithMetaGoverningLawEnum

class ContractDetails(CdmModelBase):
    """Defines specific attributes that relate to contractual details of trades."""
    documentation: List[ForwardRef("LegalAgreement")] = Field(None, description="Represents the legal document(s) that governs a trade and associated contractual product terms, either as a reference to such documents when specified as part of the CDM, or through identification of some of the key terms of those documents, such as the type of document, the document identifier, the publisher, the document vintage and the agreement date.")
    governing_law: ForwardRef("FieldWithMetaGoverningLawEnum") = Field(None, description="Represents the law governing the trade and associated contractual product terms.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
from src.models.cdm.generated.metafields.field_with_meta_governing_law_enum import FieldWithMetaGoverningLawEnum
ContractDetails.model_rebuild()
