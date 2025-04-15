from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.credit_limit_utilisation import CreditLimitUtilisation
    from src.models.cdm.generated.event.workflow.velocity import Velocity
    from src.models.cdm.generated.metafields.field_with_meta_credit_limit_type_enum import FieldWithMetaCreditLimitTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class LimitApplicable(CdmModelBase):
    """"""
    limit_type: ForwardRef("FieldWithMetaCreditLimitTypeEnum") = Field(None, description="Standard code to indicate which type of credit line is being referred to - i.e. IM, DV01, PV01, CS01, Notional, Clip Size, Notional, maximumOrderQuantity.")
    clip_size: int = Field(None, description="This element is required in FpML, optional in CDM for the purpose of accommodating the CME data representation while making reference to the FpML one.")
    amount_utilized: float = Field(None, description="The limit utilised by all the cleared trades for the limit level and limit type. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
    utilization: ForwardRef("CreditLimitUtilisation") = Field(None)
    amount_remaining: float = Field(None, description="The limit remaining for the limit level and limit type. This does not take into account any pending trades. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
    currency: ForwardRef("FieldWithMetaString") = Field(None, description="The currency in which the applicable limit is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    velocity: ForwardRef("Velocity") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.credit_limit_utilisation import CreditLimitUtilisation
from src.models.cdm.generated.event.workflow.velocity import Velocity
from src.models.cdm.generated.metafields.field_with_meta_credit_limit_type_enum import FieldWithMetaCreditLimitTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
LimitApplicable.model_rebuild()
