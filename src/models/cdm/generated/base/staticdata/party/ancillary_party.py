from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class AncillaryParty(CdmModelBase):
    """Defines an ancillary role enumerated value with an associated party reference. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and this AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference."""
    role: ForwardRef("AncillaryRoleEnum") = Field(description="Specifies the AncillaryRoleEnum that is associated to the party reference. An ancillary party is any involved party that is not one of the two principal parties to the transaction.")
    party_reference: List[ForwardRef("ReferenceWithMetaParty")] = Field(None, description="Specifies the party, or parties, associated to the ancillary role.")
    on_behalf_of: ForwardRef("CounterpartyRoleEnum") = Field(None, description="Optionally specifies the counterparty that the ancillary party is acting on behalf of.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
AncillaryParty.model_rebuild()
