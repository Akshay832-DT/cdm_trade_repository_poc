from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.addtl_attrbts import AddtlAttrbts
    from src.models.cdm.generated.regulation.buyr import Buyr
    from src.models.cdm.generated.regulation.exctg_prsn import ExctgPrsn
    from src.models.cdm.generated.regulation.fin_instrm import FinInstrm
    from src.models.cdm.generated.regulation.invstmt_dcsn_prsn import InvstmtDcsnPrsn
    from src.models.cdm.generated.regulation.ordr_trnsmssn import OrdrTrnsmssn
    from src.models.cdm.generated.regulation.sellr import Sellr
    from src.models.cdm.generated.regulation.tx import Tx

class New(CdmModelBase):
    """"""
    tx_id: str = Field()
    exctg_pty: str = Field()
    invstmt_pty_ind: str = Field()
    submitg_pty: str = Field()
    buyr: ForwardRef("Buyr") = Field()
    sellr: ForwardRef("Sellr") = Field()
    ordr_trnsmssn: ForwardRef("OrdrTrnsmssn") = Field()
    tx: ForwardRef("Tx") = Field()
    fin_instrm: ForwardRef("FinInstrm") = Field()
    invstmt_dcsn_prsn: ForwardRef("InvstmtDcsnPrsn") = Field()
    exctg_prsn: ForwardRef("ExctgPrsn") = Field()
    addtl_attrbts: ForwardRef("AddtlAttrbts") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.regulation.addtl_attrbts import AddtlAttrbts
from src.models.cdm.generated.regulation.buyr import Buyr
from src.models.cdm.generated.regulation.exctg_prsn import ExctgPrsn
from src.models.cdm.generated.regulation.fin_instrm import FinInstrm
from src.models.cdm.generated.regulation.invstmt_dcsn_prsn import InvstmtDcsnPrsn
from src.models.cdm.generated.regulation.ordr_trnsmssn import OrdrTrnsmssn
from src.models.cdm.generated.regulation.sellr import Sellr
from src.models.cdm.generated.regulation.tx import Tx
New.model_rebuild()
