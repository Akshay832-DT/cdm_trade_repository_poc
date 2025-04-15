from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference

class ReferenceWithMetaTradeState(CdmModelBase):
    """"""
    global_reference: str = Field(None)
    external_reference: str = Field(None)
    address: ForwardRef("Reference") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.rosetta.model.lib.meta.Reference.reference import Reference
ReferenceWithMetaTradeState.model_rebuild()
