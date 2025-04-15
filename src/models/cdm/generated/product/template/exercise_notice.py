from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
    from src.models.cdm.generated.product.template.exercise_notice_giver_enum import ExerciseNoticeGiverEnum

class ExerciseNotice(CdmModelBase):
    """Defines to whom and where notice of execution should be given. The exerciseNoticeGiver refers to one or both of the principal parties of the trade. If present the exerciseNoticeReceiver refers to a party, other than the principal party, to whom notice should be given."""
    exercise_notice_giver: ForwardRef("ExerciseNoticeGiverEnum") = Field(description="Specifies the principal party of the trade that has the right to exercise.")
    exercise_notice_receiver: ForwardRef("AncillaryRoleEnum") = Field(None, description="Specifies the party to which notice of exercise should be given, e.g. by the buyer of the option. Although in many cases it is the buyer of the option who sends the exercise notice to the seller of the option, this component is reused, e.g. in case of OptionEarlyTermination, either or both parties have the right to exercise.")
    business_center: ForwardRef("FieldWithMetaBusinessCenterEnum") = Field(description="Specifies the location where the exercise must be reported, e.g. where the exercise notice receiver is based.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
from src.models.cdm.generated.product.template.exercise_notice_giver_enum import ExerciseNoticeGiverEnum
ExerciseNotice.model_rebuild()
