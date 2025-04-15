from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.debt_class_enum import DebtClassEnum
    from src.models.cdm.generated.base.staticdata.asset.common.debt_economics import DebtEconomics

class DebtType(CdmModelBase):
    """Specifies the type of debt instrument."""
    debt_class: ForwardRef("DebtClassEnum") = Field(None, description="Specifies the characteristics of a debt instrument.")
    debt_economics: List[ForwardRef("DebtEconomics")] = Field(None, description="Specifies selected financial terms of a debt instrument.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.debt_class_enum import DebtClassEnum
from src.models.cdm.generated.base.staticdata.asset.common.debt_economics import DebtEconomics
DebtType.model_rebuild()
