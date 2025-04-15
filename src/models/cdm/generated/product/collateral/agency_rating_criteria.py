from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.credit_notation import CreditNotation
    from src.models.cdm.generated.observable.asset.credit_notation_boundary_enum import CreditNotationBoundaryEnum
    from src.models.cdm.generated.observable.asset.credit_notation_mismatch_resolution_enum import CreditNotationMismatchResolutionEnum
    from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum

class AgencyRatingCriteria(CdmModelBase):
    """Represents a class to specify a credit notation."""
    credit_notation: ForwardRef("CreditNotation") = Field(description="Indicates the agency rating criteria specified for the asset or issuer.")
    mismatch_resolution: ForwardRef("CreditNotationMismatchResolutionEnum") = Field(None, description="Indicator for options to be used if several agency ratings (>1) are specified and its necessary to identify specific charateristics. i.e (lowest or highest).")
    reference_agency: ForwardRef("CreditRatingAgencyEnum") = Field(None, description="identifies the dominant reference agency if there is a missmatch and several reference agencies exsist.")
    boundary: ForwardRef("CreditNotationBoundaryEnum") = Field(None, description="Indicates the boundary of a credit agency rating i.e minimum or maximum.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.credit_notation import CreditNotation
from src.models.cdm.generated.observable.asset.credit_notation_boundary_enum import CreditNotationBoundaryEnum
from src.models.cdm.generated.observable.asset.credit_notation_mismatch_resolution_enum import CreditNotationMismatchResolutionEnum
from src.models.cdm.generated.observable.asset.credit_rating_agency_enum import CreditRatingAgencyEnum
AgencyRatingCriteria.model_rebuild()
