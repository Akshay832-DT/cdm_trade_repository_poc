from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause import MasterAgreementClause

class MasterAgreementSchedule(CdmModelBase):
    """The set of elections which specify a Master Agreement."""
    clause: List[ForwardRef("MasterAgreementClause")] = Field(None, description="Clauses that have had elections made against them in this Master Agreement. There must be at least one clause defined in the agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause import MasterAgreementClause
MasterAgreementSchedule.model_rebuild()
