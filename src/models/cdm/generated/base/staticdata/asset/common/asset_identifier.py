from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_id_type_enum import AssetIdTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class AssetIdentifier(CdmModelBase):
    """The unique identifier for an Asset, specified using an Asset Identifier Type enumerator."""
    identifier: ForwardRef("FieldWithMetaString") = Field(description="The identifier value.")
    identifier_type: ForwardRef("AssetIdTypeEnum") = Field(description="Defines the symbology source of the Asset Identifier, eg CUSIP, ISIN, etc.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_id_type_enum import AssetIdTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
AssetIdentifier.model_rebuild()
