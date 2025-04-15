from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class EquityUnderlierProvisions(CdmModelBase):
    """"""
    multiple_exchange_index_annex_fallback: bool = Field(None, description="For an index option or swap transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.")
    component_security_index_annex_fallback: bool = Field(None, description="For an index option or swap transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.")
    local_jurisdiction: ForwardRef("FieldWithMetaString") = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")
    relevant_jurisdiction: ForwardRef("FieldWithMetaString") = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
EquityUnderlierProvisions.model_rebuild()
