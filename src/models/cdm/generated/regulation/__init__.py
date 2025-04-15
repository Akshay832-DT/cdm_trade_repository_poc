"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.regulation.acct_ownr import AcctOwnr
    from src.models.cdm.generated.regulation.addtl_attrbts import AddtlAttrbts
    from src.models.cdm.generated.regulation.buyr import Buyr
    from src.models.cdm.generated.regulation.deriv_instrm_attrbts import DerivInstrmAttrbts
    from src.models.cdm.generated.regulation.document import Document
    from src.models.cdm.generated.regulation.exctg_prsn import ExctgPrsn
    from src.models.cdm.generated.regulation.fin_instrm import FinInstrm
    from src.models.cdm.generated.regulation.fin_instrm_gnl_attrbts import FinInstrmGnlAttrbts
    from src.models.cdm.generated.regulation.fin_instrm_rptg_tx_rpt import FinInstrmRptgTxRpt
    from src.models.cdm.generated.regulation.id import Id
    from src.models.cdm.generated.regulation.indx import Indx
    from src.models.cdm.generated.regulation.invstmt_dcsn_prsn import InvstmtDcsnPrsn
    from src.models.cdm.generated.regulation.new import New
    from src.models.cdm.generated.regulation.nm import Nm
    from src.models.cdm.generated.regulation.ordr_trnsmssn import OrdrTrnsmssn
    from src.models.cdm.generated.regulation.othr import Othr
    from src.models.cdm.generated.regulation.pric import Pric
    from src.models.cdm.generated.regulation.prsn import Prsn
    from src.models.cdm.generated.regulation.qty import Qty
    from src.models.cdm.generated.regulation.ref_rate import RefRate
    from src.models.cdm.generated.regulation.schme_nm import SchmeNm
    from src.models.cdm.generated.regulation.sellr import Sellr
    from src.models.cdm.generated.regulation.sngl import Sngl
    from src.models.cdm.generated.regulation.swp import Swp
    from src.models.cdm.generated.regulation.swp_in import SwpIn
    from src.models.cdm.generated.regulation.swp_out import SwpOut
    from src.models.cdm.generated.regulation.term import Term
    from src.models.cdm.generated.regulation.tx import Tx
    from src.models.cdm.generated.regulation.undrlyg_instrm import UndrlygInstrm
