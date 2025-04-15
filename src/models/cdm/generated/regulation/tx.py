from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.new import New
    from src.models.cdm.generated.regulation.pric import Pric
    from src.models.cdm.generated.regulation.qty import Qty

class Tx(CdmModelBase):
    """"""
    new_tx: ForwardRef("New") = Field()
    trad_dt: str = Field()
    tradg_cpcty: str = Field()
    qty: ForwardRef("Qty") = Field()
    pric: ForwardRef("Pric") = Field()
    trad_vn: str = Field()
    ctry_of_brnch: str = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.new import New
from src.models.cdm.generated.regulation.pric import Pric
from src.models.cdm.generated.regulation.qty import Qty
Tx.model_rebuild()
