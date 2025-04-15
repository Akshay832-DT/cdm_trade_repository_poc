from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.swp_in import SwpIn
    from src.models.cdm.generated.regulation.swp_out import SwpOut

class Swp(CdmModelBase):
    """"""
    swp_in: ForwardRef("SwpIn") = Field()
    swp_out: ForwardRef("SwpOut") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.swp_in import SwpIn
from src.models.cdm.generated.regulation.swp_out import SwpOut
Swp.model_rebuild()
