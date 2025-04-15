from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.collateral_criteria import CollateralCriteria
    from src.models.cdm.generated.product.collateral.all_criteria import AllCriteria
    from src.models.cdm.generated.product.collateral.any_criteria import AnyCriteria
    from src.models.cdm.generated.product.collateral.sovereign_agency_rating import SovereignAgencyRating

class NegativeCriteria(CdmModelBase):
    """Used to apply a NOT logic condition to a single Collateral Criteria."""
    negative_criteria: ForwardRef("CollateralCriteria") = Field()

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.collateral_criteria import CollateralCriteria
from src.models.cdm.generated.product.collateral.all_criteria import AllCriteria
from src.models.cdm.generated.product.collateral.any_criteria import AnyCriteria
from src.models.cdm.generated.product.collateral.sovereign_agency_rating import SovereignAgencyRating
NegativeCriteria.model_rebuild()
