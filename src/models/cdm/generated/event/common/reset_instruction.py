from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout

class ResetInstruction(CdmModelBase):
    """Defines the information needed to create a Reset Business Event. """
    payout: List[ForwardRef("ReferenceWithMetaPayout")] = Field(None)
    rate_record_date: str = Field(None, description="Specifies the 'Rate Record Day' for a Fallback rate.  Fallback rate fixing processes typically set the fixing rate in arrears, i.e., the Fallback Rate corresponding to a Rate Record Date is set at the end of the interest accural period.  When this applies, Reset->resetDate occurs at the end of the interest period, and the Reset->rateRecordDate occurs near the start of the interest period.  The Reset->rateRecordDate and Reset->observations->observationIdentifier->observationDate will differ if a Fallback rate is unavailable on the Rate Record Date, and the latest previous available rate is used as the observation.")
    reset_date: str = Field(description="Specifies the date on which the reset is occuring.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_payout import ReferenceWithMetaPayout
ResetInstruction.model_rebuild()
