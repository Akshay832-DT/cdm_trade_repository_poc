from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key

class MetaFields(CdmModelBase):
    """"""
    scheme: str = Field(None)
    global_key: str = Field(None)
    external_key: str = Field(None)
    key: List[ForwardRef("Key")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.rosetta.model.lib.meta.Key.key import Key
MetaFields.model_rebuild()
