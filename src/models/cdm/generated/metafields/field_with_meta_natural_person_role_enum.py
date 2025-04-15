from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.natural_person_role_enum import NaturalPersonRoleEnum
    from src.models.cdm.generated.metafields.meta_fields import MetaFields

class FieldWithMetaNaturalPersonRoleEnum(CdmModelBase):
    """"""
    value: ForwardRef("NaturalPersonRoleEnum") = Field(None)
    meta: ForwardRef("MetaFields") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.natural_person_role_enum import NaturalPersonRoleEnum
from src.models.cdm.generated.metafields.meta_fields import MetaFields
FieldWithMetaNaturalPersonRoleEnum.model_rebuild()
