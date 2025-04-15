from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_entity_type_enum import FieldWithMetaEntityTypeEnum
    from src.models.cdm.generated.product.asset.reference_obligation import ReferenceObligation

class ReferencePair(CdmModelBase):
    """"""
    reference_entity: ForwardRef("LegalEntity") = Field(description="The corporate or sovereign entity on which you are buying or selling protection and any successor that assumes all or substantially all of its contractual and other obligations. It is vital to use the correct legal name of the entity and to be careful not to choose a subsidiary if you really want to trade protection on a parent company. Please note, Reference Entities cannot be senior or subordinated. It is the obligations of the Reference Entities that can be senior or subordinated. ISDA 2003 Term: Reference Entity.")
    reference_obligation: ForwardRef("ReferenceObligation") = Field(None, description="The Reference Obligation is a financial instrument that is either issued or guaranteed by the reference entity. It serves to clarify the precise reference entity protection is being offered upon, and its legal position with regard to other related firms (parents/subsidiaries). Furthermore the Reference Obligation is ALWAYS deliverable and establishes the Pari Passu ranking (as the deliverable bonds must rank equal to the reference obligation). ISDA 2003 Term: Reference Obligation.")
    no_reference_obligation: bool = Field(None, description="Used to indicate that there is no Reference Obligation associated with this Credit Default Swap and that there will never be one.")
    entity_type: ForwardRef("FieldWithMetaEntityTypeEnum") = Field(description="Defines the reference entity types corresponding to a list of types in the ISDA First to Default documentation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_entity_type_enum import FieldWithMetaEntityTypeEnum
from src.models.cdm.generated.product.asset.reference_obligation import ReferenceObligation
ReferencePair.model_rebuild()
