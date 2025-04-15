from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.asset.bounded_variance import BoundedVariance

class VarianceCapFloor(CdmModelBase):
    """"""
    variance_cap: bool = Field(description="If present and true, then variance cap is applicable.")
    unadjusted_variance_cap: float = Field(None, description="For use when varianceCap is applicable. Contains the scaling factor of the Variance Cap that can differ on a trade-by-trade basis in the European market. For example, a Variance Cap of 2.5^2 x Variance Strike Price has an unadjustedVarianceCap of 2.5.")
    bounded_variance: ForwardRef("BoundedVariance") = Field(None, description="Conditions which bound variance. The contract specifies one or more boundary levels. These levels are expressed as prices for confirmation purposes Underlyer price must be equal to or higher than Lower Barrier is known as Up Conditional Swap Underlyer price must be equal to or lower than Upper Barrier is known as Down Conditional Swap Underlyer price must be equal to or higher than Lower Barrier and must be equal to or lower than Upper Barrier is known as Barrier Conditional Swap.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.asset.bounded_variance import BoundedVariance
VarianceCapFloor.model_rebuild()
