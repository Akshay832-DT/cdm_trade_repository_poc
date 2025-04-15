from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.ref_rate import RefRate
    from src.models.cdm.generated.regulation.term import Term

class Nm(CdmModelBase):
    """"""
    ref_rate: ForwardRef("RefRate") = Field()
    term: ForwardRef("Term") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.ref_rate import RefRate
from src.models.cdm.generated.regulation.term import Term
Nm.model_rebuild()
