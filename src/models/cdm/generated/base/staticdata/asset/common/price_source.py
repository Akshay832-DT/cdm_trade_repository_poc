from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class PriceSource(CdmModelBase):
    """Specifies a publication that provides the commodity price, including, where applicable, the details of where in the publication the price is published."""
    price_publisher: ForwardRef("FieldWithMetaString") = Field(description="Defines a publication in which the price can be found. (e.g Gas Daily, Platts Bloomberg. Commodity publishers can be found at this URL:  http://www.fpml.org/coding-scheme/commodity-information-provider>")
    price_source_location: str = Field(None, description="Specifies the location of the price which may be a specific page, electornic screen name, or a code (e.g. a RIC code) where the price can be found.")
    price_source_heading: str = Field(None, description="Specifies the heading or field name for the price  on a given page or screen, where applicable.")
    price_source_time: str = Field(None, description="Specifies the time at which the price should be observed.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
PriceSource.model_rebuild()
