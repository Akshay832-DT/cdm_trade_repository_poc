from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.prsn import Prsn

class InvstmtDcsnPrsn(CdmModelBase):
    """"""
    prsn: ForwardRef("Prsn") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.prsn import Prsn
InvstmtDcsnPrsn.model_rebuild()
