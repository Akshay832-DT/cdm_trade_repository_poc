from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.position.position_status_enum import PositionStatusEnum
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
    from src.models.cdm.generated.metafields.reference_with_meta_trade import ReferenceWithMetaTrade
    from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct

class AggregationParameters(CdmModelBase):
    """ Parameters to be used to filter events that are relevant to a given portfolio in order to calculate the state of this portfolio. The attributes correspond to all the possible aggregation criteria that can be used and these criteria can be combined. All the attributes are optional."""
    date_time: str = Field(description="To aggregate as of a particular date")
    total_position: bool = Field(None, description="Specifies whether to calculate total position to given date, or only daily position for the given date.")
    position_status: ForwardRef("PositionStatusEnum") = Field(None, description="To aggregate based on position status (EXECUTED, SETTLED etc)")
    party: List[ForwardRef("ReferenceWithMetaParty")] = Field(None, description="To aggregate based on a selection of party(ies) / legal entity(ies).")
    product: List[ForwardRef("NonTransferableProduct")] = Field(None, description="To aggregate based on a selection of products.")
    product_qualifier: List[List] = Field(None, description="To aggregate based on a selection of product type(s).")
    trade_reference: List[ForwardRef("ReferenceWithMetaTrade")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.position.position_status_enum import PositionStatusEnum
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
from src.models.cdm.generated.metafields.reference_with_meta_trade import ReferenceWithMetaTrade
from src.models.cdm.generated.product.template.non_transferable_product import NonTransferableProduct
AggregationParameters.model_rebuild()
