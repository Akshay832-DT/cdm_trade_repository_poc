from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity

class AncillaryEntity(CdmModelBase):
    """Holds an identifier for an ancillary entity, either identified directly via its ancillary role or directly as a legal entity."""
    ancillary_party: ForwardRef("AncillaryRoleEnum") = Field(None, description="Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)")
    legal_entity: ForwardRef("LegalEntity") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
AncillaryEntity.model_rebuild()
