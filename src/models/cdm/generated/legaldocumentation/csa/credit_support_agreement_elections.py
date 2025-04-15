from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class CreditSupportAgreementElections(CdmModelBase):
    """The set of elections which specify a Credit Support Annex or Deed."""

# Import after class definition to avoid circular imports
CreditSupportAgreementElections.model_rebuild()
