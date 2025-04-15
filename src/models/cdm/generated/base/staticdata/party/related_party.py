from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_account import ReferenceWithMetaAccount
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class RelatedParty(CdmModelBase):
    """"""
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(description="Reference to a party.")
    account_reference: ForwardRef("ReferenceWithMetaAccount") = Field(None, description="Reference to an account.")
    role: ForwardRef("PartyRoleEnum") = Field(description="The category of the relationship. The related party performs the role specified in this field for the base party. For example, if the role is ,Guarantor, the related party acts as a guarantor for the base party.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_account import ReferenceWithMetaAccount
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
RelatedParty.model_rebuild()
