from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.product.common.settlement.percentage_rule import PercentageRule

class PaymentRule(CdmModelBase):
    """A class defining the payment calculation rule. As of FpML 5.10, percentage rule is the only calculation rule that has been specified as part of the standard."""
    percentage_rule: ForwardRef("PercentageRule") = Field(None, description="This attribute is not present as part of the FpML construct, as the payment rule is specialised by means of runtime type extension through the xsi:type.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.product.common.settlement.percentage_rule import PercentageRule
PaymentRule.model_rebuild()
