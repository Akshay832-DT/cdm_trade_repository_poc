from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class IndexBase(CdmModelBase):
    """Identifies an index by referencing an identifier."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    name: ForwardRef("FieldWithMetaString") = Field(None, description="A description of the Index.")
    provider: ForwardRef("LegalEntity") = Field(None, description="The organisation that creates or maintains the Index.")
    asset_class: ForwardRef("AssetClassEnum") = Field(None, description="The Asset Class of the Index.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
IndexBase.model_rebuild()
