from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria

class SovereignAgencyRating(CdmModelBase):
    """Represents a sovereign agency rating based on default risk of the country of the issuer."""
    sovereign_agency_rating: Optional[ForwardRef("AgencyRatingCriteria")] = Field(None, description="Represents an agency rating based on default risk of the country of the issuer.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria
SovereignAgencyRating.model_rebuild()
