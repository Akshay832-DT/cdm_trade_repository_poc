from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria

class AssetAgencyRating(CdmModelBase):
    """"""
    asset_agency_rating: ForwardRef("AgencyRatingCriteria") = Field(description="Represents an agency rating based on default risk and creditors claim in event of default associated with specific instrument.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.agency_rating_criteria import AgencyRatingCriteria
AssetAgencyRating.model_rebuild()
