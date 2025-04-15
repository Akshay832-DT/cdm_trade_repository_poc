from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity

class IssuerName(CdmModelBase):
    """"""
    issuer_name: ForwardRef("LegalEntity") = Field(description="Specifies the issuing entity name or LEI.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
IssuerName.model_rebuild()
