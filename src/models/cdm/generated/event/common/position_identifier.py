from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
    from src.models.cdm.generated.base.staticdata.identifier.trade_identifier_type_enum import TradeIdentifierTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class PositionIdentifier(CdmModelBase):
    """Defines a position identifier as a special case of the generic identifier type, that also includes the position identifier class."""
    issuer_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="The identifier issuer, when specified by reference to a party specified as part of the transaction.")
    issuer: ForwardRef("FieldWithMetaString") = Field(None, description="The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).")
    assigned_identifier: List[ForwardRef("AssignedIdentifier")] = Field(None, description="The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.")
    identifier_type: ForwardRef("TradeIdentifierTypeEnum") = Field(None, description="The enumerated classification of the identifier. Optional as a position identifier may be party-specific, in which case it may not correspond to any established classification.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.assigned_identifier import AssignedIdentifier
from src.models.cdm.generated.base.staticdata.identifier.trade_identifier_type_enum import TradeIdentifierTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
PositionIdentifier.model_rebuild()
