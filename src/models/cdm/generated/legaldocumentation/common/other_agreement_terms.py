from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class OtherAgreementTerms(CdmModelBase):
    """A class to specify a related legal agreement. For example, ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (s): Other CSA and Japanese Law CSA (VM). | ISDA 2016 Credit Support Annex for Variation Margin, paragraph 13, (o): Other CSA."""
    is_specified: bool = Field(description="The qualification of whether some other related agreement is specified (True) or not (False).")
    legal_document: str = Field(None, description="The specification of this other agreement, when the qualification is True.")

# Import after class definition to avoid circular imports
OtherAgreementTerms.model_rebuild()
