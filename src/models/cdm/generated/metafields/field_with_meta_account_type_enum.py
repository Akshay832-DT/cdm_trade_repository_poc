from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.account_type_enum import AccountTypeEnum
    from src.models.cdm.generated.metafields.meta_fields import MetaFields

class FieldWithMetaAccountTypeEnum(CdmModelBase):
    """"""
    value: ForwardRef("AccountTypeEnum") = Field(None)
    meta: ForwardRef("MetaFields") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.account_type_enum import AccountTypeEnum
from src.models.cdm.generated.metafields.meta_fields import MetaFields
FieldWithMetaAccountTypeEnum.model_rebuild()
