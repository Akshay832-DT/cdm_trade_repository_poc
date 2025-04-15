from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.indx import Indx

class Sngl(CdmModelBase):
    """"""
    isin: str = Field()
    indx: ForwardRef("Indx") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.indx import Indx
Sngl.model_rebuild()
