from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class ListingExchange(CdmModelBase):
    """Specifies a filter based on a stock exchange."""
    exchange: List[ForwardRef("FieldWithMetaString")] = Field(None, description="Represents a filter based on the Primary Stock Exchange facilitating the listing of companies, exchange of Stocks, Exchange traded Derivatives, Bonds, and other Securities expressed in ISO standard 10383.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
ListingExchange.model_rebuild()
