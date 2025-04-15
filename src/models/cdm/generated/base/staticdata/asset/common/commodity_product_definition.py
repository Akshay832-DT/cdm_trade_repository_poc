from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.commodity_information_publisher_enum import CommodityInformationPublisherEnum
    from src.models.cdm.generated.base.staticdata.asset.common.commodity_reference_framework import CommodityReferenceFramework
    from src.models.cdm.generated.base.staticdata.asset.common.price_source import PriceSource
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class CommodityProductDefinition(CdmModelBase):
    """Specifies the commodity underlier in the event that no ISDA Commodity Reference Price exists."""
    reference_framework: ForwardRef("CommodityReferenceFramework") = Field(description="Specifies the type of commodity.")
    price_source: ForwardRef("PriceSource") = Field(None, description="Specifies a publication that provides the commodity price, including, where applicable the details of where in the publication the price is published.  Applicable when the commodity reference price is not a futures contract")
    commodity_info_publisher: ForwardRef("CommodityInformationPublisherEnum") = Field(None, description="Specifies the publication where the commodity prices can be found.")
    exchange_id: ForwardRef("FieldWithMetaString") = Field(description=" Identifies the exchange from which the reference price should be sourced, using the scheme at the following url: http://www.fpml.org/coding-scheme/external/exchange-id-MIC-1-0")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.commodity_information_publisher_enum import CommodityInformationPublisherEnum
from src.models.cdm.generated.base.staticdata.asset.common.commodity_reference_framework import CommodityReferenceFramework
from src.models.cdm.generated.base.staticdata.asset.common.price_source import PriceSource
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
CommodityProductDefinition.model_rebuild()
