from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_date import AdjustableOrAdjustedDate
    from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
    from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction
    from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
    from src.models.cdm.generated.metafields.reference_with_meta_option_payout import ReferenceWithMetaOptionPayout

class ExerciseInstruction(CdmModelBase):
    """Specifies the information required to communicate the choices made by the exercising party, in a financial product endowing the party with at least one option."""
    exercise_quantity: ForwardRef("PrimitiveInstruction") = Field(description="Contains instructions for exercising the option including a quantity change, and optionally a transfer.")
    exercise_option: ForwardRef("ReferenceWithMetaOptionPayout") = Field(None, description="Specifies the Option Payout being exercised on the trade.")
    exercise_date: ForwardRef("AdjustableOrAdjustedDate") = Field(None, description="Specifies the date on which an option contained within the financial product would be exercised. The date may be omitted if the contractual product allows for only a single date of exercise (European exercise).")
    exercise_time: ForwardRef("BusinessCenterTime") = Field(None, description="Specifies the time at which an option contained within the financial product woulld be exercised. The time may be omitted if the contractual product allows for only a single time of exercise (European exercise). ")
    replacement_trade_identifier: List[ForwardRef("TradeIdentifier")] = Field(None, description="Specifies the trade identifier to apply to the replacement trade for physical exercise.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.adjustable_or_adjusted_date import AdjustableOrAdjustedDate
from src.models.cdm.generated.base.datetime.business_center_time import BusinessCenterTime
from src.models.cdm.generated.event.common.primitive_instruction import PrimitiveInstruction
from src.models.cdm.generated.event.common.trade_identifier import TradeIdentifier
from src.models.cdm.generated.metafields.reference_with_meta_option_payout import ReferenceWithMetaOptionPayout
ExerciseInstruction.model_rebuild()
