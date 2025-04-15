from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.product_id_type_enum import ProductIdTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class ProductIdentifier(CdmModelBase):
    """Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage."""
    identifier: ForwardRef("FieldWithMetaString") = Field(description="Provides an identifier associated with a specific product.  The identifier is unique within the public source specified in the source attribute.")
    source: ForwardRef("ProductIdTypeEnum") = Field(description="Defines the source of the identifier.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.product_id_type_enum import ProductIdTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
ProductIdentifier.model_rebuild()
