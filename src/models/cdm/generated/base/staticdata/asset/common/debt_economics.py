from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.debt_interest_enum import DebtInterestEnum
    from src.models.cdm.generated.base.staticdata.asset.common.debt_principal_enum import DebtPrincipalEnum
    from src.models.cdm.generated.base.staticdata.asset.common.debt_seniority_enum import DebtSeniorityEnum

class DebtEconomics(CdmModelBase):
    """Specifies selected economics of a debt instrument."""
    debt_seniority: ForwardRef("DebtSeniorityEnum") = Field(None, description="Specifies the order of repayment in the event of a sale or bankruptcy of the issuer or a related party (eg guarantor).")
    debt_interest: ForwardRef("DebtInterestEnum") = Field(None, description="Specifies the general rule for periodic interest rate payment.")
    debt_principal: ForwardRef("DebtPrincipalEnum") = Field(None, description="Specifies the general rule for repayment of principal.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.debt_interest_enum import DebtInterestEnum
from src.models.cdm.generated.base.staticdata.asset.common.debt_principal_enum import DebtPrincipalEnum
from src.models.cdm.generated.base.staticdata.asset.common.debt_seniority_enum import DebtSeniorityEnum
DebtEconomics.model_rebuild()
