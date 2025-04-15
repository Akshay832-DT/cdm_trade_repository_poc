from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.quantifier_enum import QuantifierEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class MultipleDebtTypes(CdmModelBase):
    """Represents a class to specify multiple credit debt types alongside a conditional 'any' or 'all' qualifier."""
    condition: ForwardRef("QuantifierEnum") = Field(description="An enumerated attribute, to qualify whether All or Any debt type applies.")
    debt_type: List[ForwardRef("FieldWithMetaString")] = Field(None, description="The type of debt, e.g. long term debt, deposit, ... FpML doesn't specific a scheme value, hence no enumeration is specified as part of the CDM. At least two debt types much be specified.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.quantifier_enum import QuantifierEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
MultipleDebtTypes.model_rebuild()
