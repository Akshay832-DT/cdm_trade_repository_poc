from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.collateral.collateral_interest_parameters import CollateralInterestParameters

class DistributionAndInterestPayment(CdmModelBase):
    """A class to specify the Distributions and Interest Payment provisions applicable to the collateral agreement."""
    interest_parameters: List[ForwardRef("CollateralInterestParameters")] = Field(None, description="Represents the interest parameters for the various currencies, margin types, posting parties.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.collateral.collateral_interest_parameters import CollateralInterestParameters
DistributionAndInterestPayment.model_rebuild()
