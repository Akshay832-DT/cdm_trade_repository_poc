from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class FinancialUnitEnum(CdmModelBase):
    """Provides enumerated values for financial units, generally used in the context of defining quantities for securities."""
    # Enum values
    Contract: ClassVar[str] = "Contract"
    ContractualProduct: ClassVar[str] = "ContractualProduct"
    IndexUnit: ClassVar[str] = "IndexUnit"
    LogNormalVolatility: ClassVar[str] = "LogNormalVolatility"
    Share: ClassVar[str] = "Share"
    ValuePerDay: ClassVar[str] = "ValuePerDay"
    ValuePerPercent: ClassVar[str] = "ValuePerPercent"
    Weight: ClassVar[str] = "Weight"


# Import after class definition to avoid circular imports
FinancialUnitEnum.model_rebuild()
