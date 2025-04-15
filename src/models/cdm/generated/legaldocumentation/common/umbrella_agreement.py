from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement_entity import UmbrellaAgreementEntity

class UmbrellaAgreement(CdmModelBase):
    """A class to specify a set of legal entities which are part of a legal agreement beyond the two contracting parties to that agreement. This data representation reflects the ISDA Create representation."""
    is_applicable: bool = Field(description="The determination of whether Umbrella Agreement terms are Applicable (True), or Not Applicable (False)")
    language: str = Field(None, description="The language associated with the umbrella agreement, and which applies to all the parties to the umbrella agreement.")
    parties: List[ForwardRef("UmbrellaAgreementEntity")] = Field(None, description="Underlying principals to the umbrella agreement.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement_entity import UmbrellaAgreementEntity
UmbrellaAgreement.model_rebuild()
