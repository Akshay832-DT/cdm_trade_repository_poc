from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_classification import TaxonomyClassification
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class TaxonomyValue(CdmModelBase):
    """Defines a taxonomy value as either a simple string or a more granular expression with class names and values for each class."""
    name: ForwardRef("FieldWithMetaString") = Field(None, description="Specifies the taxonomy value as a simple string, which may be associated to an external scheme.")
    classification: List[ForwardRef("TaxonomyClassification")] = Field(None, description="Specifies the taxonomy value as a set of class names and values for each class.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_classification import TaxonomyClassification
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
TaxonomyValue.model_rebuild()
