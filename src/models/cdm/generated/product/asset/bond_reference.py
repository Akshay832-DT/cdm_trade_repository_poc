from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.security import Security
    from src.models.cdm.generated.product.asset.fixed_rate_specification import FixedRateSpecification

class BondReference(CdmModelBase):
    """Reference to a bond underlier to represent an asset swap or Condition Precedent Bond."""
    bond: ForwardRef("Security") = Field(description="Reference to a bond underlier.")
    condition_precedent_bond: bool = Field(description="To indicate whether the Condition Precedent Bond is applicable. The swap contract is only valid if the bond is issued and if there is any dispute over the terms of fixed stream then the bond terms would be used.")
    discrepancy_clause: bool = Field(None, description="To indicate whether the Discrepancy Clause is applicable.")
    coupon_rate: ForwardRef("FixedRateSpecification") = Field(None, description="Specifies the coupon rate (expressed in percentage) of a fixed income security or convertible bond.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
from src.models.cdm.generated.product.asset.fixed_rate_specification import FixedRateSpecification
BondReference.model_rebuild()
