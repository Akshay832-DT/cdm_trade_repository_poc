from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.resource_type_enum import ResourceTypeEnum
    from src.models.cdm.generated.metafields.meta_fields import MetaFields

class FieldWithMetaResourceTypeEnum(CdmModelBase):
    """"""
    value: ForwardRef("ResourceTypeEnum") = Field(None)
    meta: ForwardRef("MetaFields") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.resource_type_enum import ResourceTypeEnum
from src.models.cdm.generated.metafields.meta_fields import MetaFields
FieldWithMetaResourceTypeEnum.model_rebuild()
