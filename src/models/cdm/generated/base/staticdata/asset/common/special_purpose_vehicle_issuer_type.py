from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.credit_risk_enum import CreditRiskEnum

class SpecialPurposeVehicleIssuerType(CdmModelBase):
    """Represents a class to allow specification of different types of special purpose vehicle (SPV) collateral."""
    credit_risk: ForwardRef("CreditRiskEnum") = Field(None, description="Indicates tranched or untranched credit risk.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.credit_risk_enum import CreditRiskEnum
SpecialPurposeVehicleIssuerType.model_rebuild()
