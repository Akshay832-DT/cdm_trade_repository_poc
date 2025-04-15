from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class Counterparty(CdmModelBase):
    """Defines a counterparty enumerated value, e.g. Party1 or Party2, with an associated party reference. The product is agnostic to the actual parties to the transaction, with the party references abstracted away from the product definition and replaced by the CounterpartyEnum (e.g. values Party1 or Party2). The CounterpartyEnum can then be positioned in the product (e.g. to specify which counterparty is the payer, receiver etc) and this Counterparty type, which is positioned outside of the product definition, allows the CounterpartyEnum to be associated with an actual party reference."""
    role: ForwardRef("CounterpartyRoleEnum") = Field(description="Specifies the CounterpartyEnum, e.g. either Party1 or Party2, that is associated to the partyReference.")
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(description="Specifies the party that is associated to the counterparty.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
Counterparty.model_rebuild()
