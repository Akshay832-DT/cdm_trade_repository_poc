from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FinInstrmGnlAttrbts(CdmModelBase):
    """"""
    full_nm: str = Field()
    clssfctn_tp: str = Field()
    ntnl_ccy: str = Field()

# Import after class definition to avoid circular imports
FinInstrmGnlAttrbts.model_rebuild()
