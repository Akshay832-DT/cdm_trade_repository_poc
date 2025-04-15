from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class PartyRole(CdmModelBase):
    """A class to specify the role(s) that party(ies) may have in relation to the execution, contract or other legal agreement."""
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(description="A reference to the party to which the role refers to.")
    role: ForwardRef("PartyRoleEnum") = Field(description="The party role.")
    ownership_party_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="A reference to the party that has ownership of this party role information. FpML specifies that For shared trade information, this attribute will reference the originator of the data (for example, an execution facility or clearing house).")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
PartyRole.model_rebuild()
