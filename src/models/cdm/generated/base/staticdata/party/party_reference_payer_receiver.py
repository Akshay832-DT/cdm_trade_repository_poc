from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_account import ReferenceWithMetaAccount
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class PartyReferencePayerReceiver(CdmModelBase):
    """Specifies the parties responsible for making and receiving payments defined by this structure."""
    payer_party_reference: ForwardRef("ReferenceWithMetaParty") = Field(description="The party responsible for making the payments defined by this structure.")
    payer_account_reference: ForwardRef("ReferenceWithMetaAccount") = Field(None, description="A reference to the account responsible for making the payments defined by this structure.")
    receiver_party_reference: ForwardRef("ReferenceWithMetaParty") = Field(description="The party that receives the payments corresponding to this structure.")
    receiver_account_reference: ForwardRef("ReferenceWithMetaAccount") = Field(None, description="A reference to the account that receives the payments corresponding to this structure.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_account import ReferenceWithMetaAccount
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
PartyReferencePayerReceiver.model_rebuild()
