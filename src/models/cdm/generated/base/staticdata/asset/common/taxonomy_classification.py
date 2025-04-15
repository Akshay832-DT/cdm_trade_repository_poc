from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class TaxonomyClassification(CdmModelBase):
    """"""
    class_name: str = Field(None, description="The name defined by the classification system for a specific attribute in the taxonomy")
    value: str = Field(description="The value set by the taxonomy that is specific to the className attribute.")
    description: str = Field(None, description="A description of the class.")
    ordinal: int = Field(None, description="In the case of multi-layered hierarchical classification systems such as commodity classification, the layer the value and className occupy in the classification hierarchy, where 1 represents the top-layer.")

# Import after class definition to avoid circular imports
TaxonomyClassification.model_rebuild()
