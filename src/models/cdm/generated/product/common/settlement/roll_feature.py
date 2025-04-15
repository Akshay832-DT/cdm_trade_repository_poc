from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.datetime.offset import Offset
    from src.models.cdm.generated.product.asset.roll_source_calendar_enum import RollSourceCalendarEnum

class RollFeature(CdmModelBase):
    """Used in conjunction with an exchange-based pricing source. Identifies a way in which the futures contracts referenced will roll between periods. """
    roll_source_calendar: ForwardRef("RollSourceCalendarEnum") = Field(None, description="Used in conjunction with an exchange-based pricing source. Identifies a date source calendar from which the pricing dates and thus roll to the next contract will be based off (e.g. pricing is based on the NYMEX WTI First Nearby Futures Contract, if Future is chosen, the pricing will roll to the next futures contract on expiration, if ListedOption is chosen, the pricing will roll to the next futures contract on the Option expiration date which is three business days before the expiration of the NYMEX WTI futures contract.) Omitting this element will result in the default behavior expected with the pricing source described within the commodity element.")
    delivery_date_roll_convention: ForwardRef("Offset") = Field(None, description="Specifies, for a Commodity Transaction that references a delivery date for a listed future, the day on which the specified future will roll to the next nearby month prior to the expiration of the referenced future. If the future will not roll at all - i.e. the price will be taken from the expiring contract, 0 should be specified here. If the future will roll to the next nearby on the last trading day - i.e. the price will be taken from the next nearby on the last trading day, then 1 should be specified and so on.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.datetime.offset import Offset
from src.models.cdm.generated.product.asset.roll_source_calendar_enum import RollSourceCalendarEnum
RollFeature.model_rebuild()
