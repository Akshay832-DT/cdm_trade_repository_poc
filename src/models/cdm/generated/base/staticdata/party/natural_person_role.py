from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_natural_person_role_enum import FieldWithMetaNaturalPersonRoleEnum
    from src.models.cdm.generated.metafields.reference_with_meta_natural_person import ReferenceWithMetaNaturalPerson

class NaturalPersonRole(CdmModelBase):
    """A class to specify the role(s) that natural person(s) may have in relation to the contract."""
    person_reference: ForwardRef("ReferenceWithMetaNaturalPerson") = Field(description="A reference to the natural person to whom the role refers to.")
    role: List[ForwardRef("FieldWithMetaNaturalPersonRoleEnum")] = Field(None, description="FpML specifies a person role that is distinct from the party role.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_natural_person_role_enum import FieldWithMetaNaturalPersonRoleEnum
from src.models.cdm.generated.metafields.reference_with_meta_natural_person import ReferenceWithMetaNaturalPerson
NaturalPersonRole.model_rebuild()
