from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class Identifier(CdmModelBase):
    """A class to specify a generic identifier, applicable to CDM artefacts such as executions, contracts, lifecycle events and legal documents. An issuer can be associated with the actual identifier value as a way to properly qualify it."""
    issuer_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="The identifier issuer, when specified by reference to a party specified as part of the transaction.")
    issuer: ForwardRef("FieldWithMetaString") = Field(None, description="The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).")
    assigned_identifier: List[ForwardRef("AssignedIdentifier")] = Field(None, description="The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
Identifier.model_rebuild()
