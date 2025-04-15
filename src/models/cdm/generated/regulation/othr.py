from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.deriv_instrm_attrbts import DerivInstrmAttrbts
    from src.models.cdm.generated.regulation.fin_instrm_gnl_attrbts import FinInstrmGnlAttrbts
    from src.models.cdm.generated.regulation.schme_nm import SchmeNm

class Othr(CdmModelBase):
    """"""
    fin_instrm_gnl_attrbts: ForwardRef("FinInstrmGnlAttrbts") = Field()
    deriv_instrm_attrbts: ForwardRef("DerivInstrmAttrbts") = Field()
    id: str = Field()
    schme_nm: ForwardRef("SchmeNm") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.deriv_instrm_attrbts import DerivInstrmAttrbts
from src.models.cdm.generated.regulation.fin_instrm_gnl_attrbts import FinInstrmGnlAttrbts
from src.models.cdm.generated.regulation.schme_nm import SchmeNm
Othr.model_rebuild()
