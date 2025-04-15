from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.capacity_unit_enum import CapacityUnitEnum
    from src.models.cdm.generated.base.math.weather_unit_enum import WeatherUnitEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class CommodityReferenceFramework(CdmModelBase):
    """Specifies the type of commodity."""
    commodity_name: str = Field(description="Identifies the commodity more specifically. Where possible, this should follow the naming convention used in the 2005 ISDA Commodity Definitions SubAnnex A, including the subCommodity and additional qualifiers, but should be limited to 256 characters or less.")
    capacity_unit: ForwardRef("CapacityUnitEnum") = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
    weather_unit: ForwardRef("WeatherUnitEnum") = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
    currency: ForwardRef("FieldWithMetaString") = Field(description="Defines the currency in which the commodity is priced.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.capacity_unit_enum import CapacityUnitEnum
from src.models.cdm.generated.base.math.weather_unit_enum import WeatherUnitEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
CommodityReferenceFramework.model_rebuild()
