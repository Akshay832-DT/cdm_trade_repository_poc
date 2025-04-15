from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AddtlAttrbts(CdmModelBase):
    """"""
    rsk_rdcg_tx: str = Field()
    scties_fincg_tx_ind: str = Field()

# Import after class definition to avoid circular imports
AddtlAttrbts.model_rebuild()
