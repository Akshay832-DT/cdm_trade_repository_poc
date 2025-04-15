from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.credit_limit_utilisation import CreditLimitUtilisation
    from src.models.cdm.generated.event.workflow.velocity import Velocity
    from src.models.cdm.generated.metafields.field_with_meta_credit_limit_type_enum import FieldWithMetaCreditLimitTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_limit_level_enum import FieldWithMetaLimitLevelEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class LimitApplicableExtended(CdmModelBase):
    """A class to represent the CDM attributes that are not part of the FpML standard. Once broader usage is confirmed, it is expected that those two classes can be collapsed."""
    limit_type: ForwardRef("FieldWithMetaCreditLimitTypeEnum") = Field(None, description="Standard code to indicate which type of credit line is being referred to - i.e. IM, DV01, PV01, CS01, Notional, Clip Size, Notional, maximumOrderQuantity.")
    clip_size: int = Field(None, description="This element is required in FpML, optional in CDM for the purpose of accommodating the CME data representation while making reference to the FpML one.")
    amount_utilized: float = Field(None, description="The limit utilised by all the cleared trades for the limit level and limit type. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
    utilization: ForwardRef("CreditLimitUtilisation") = Field(None)
    amount_remaining: float = Field(None, description="The limit remaining for the limit level and limit type. This does not take into account any pending trades. While the attribute is of type integer in FpML and the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
    currency: ForwardRef("FieldWithMetaString") = Field(None, description="The currency in which the applicable limit is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    velocity: ForwardRef("Velocity") = Field(None)
    limit_level: ForwardRef("FieldWithMetaLimitLevelEnum") = Field(None, description="The level at which the limit is set: customer business, proprietary business or account level. This attribute is specified as a string as part of the CME clearing confirmation specification.")
    limit_amount: float = Field(None, description="The total limit available for the limit level and limit type. While the attribute is of type integer in the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")
    limit_impact_due_to_trade: float = Field(None, description="The limit utilized by this specific trade. While the attribute is of type integer in the CME schema, it has been specified to be of type number in the CDM to take into consideration java size limits as well as for consistency purposes with the way most monetary amounts are expressed.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.credit_limit_utilisation import CreditLimitUtilisation
from src.models.cdm.generated.event.workflow.velocity import Velocity
from src.models.cdm.generated.metafields.field_with_meta_credit_limit_type_enum import FieldWithMetaCreditLimitTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_limit_level_enum import FieldWithMetaLimitLevelEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
LimitApplicableExtended.model_rebuild()
