from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_value import TaxonomyValue

class Taxonomy(CdmModelBase):
    """Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object)."""
    source: ForwardRef("TaxonomySourceEnum") = Field(None, description="The source of the taxonomy that defines the rules for classifying the object. The taxonomy source is taken from a enumerated list of taxonomy names. Optional as the taxonomy source may not be provided.")
    value: ForwardRef("TaxonomyValue") = Field(None, description="The value according to that taxonomy. Optional as it may not be possible to classify the object in that taxonomy.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_source_enum import TaxonomySourceEnum
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy_value import TaxonomyValue
Taxonomy.model_rebuild()
