from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.math.capacity_unit_enum import CapacityUnitEnum
    from src.models.cdm.generated.base.math.financial_unit_enum import FinancialUnitEnum
    from src.models.cdm.generated.base.math.weather_unit_enum import WeatherUnitEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class UnitType(CdmModelBase):
    """Defines the unit to be used for price, quantity, or other purposes"""
    capacity_unit: ForwardRef("CapacityUnitEnum") = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
    weather_unit: ForwardRef("WeatherUnitEnum") = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
    financial_unit: ForwardRef("FinancialUnitEnum") = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
    currency: ForwardRef("FieldWithMetaString") = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.math.capacity_unit_enum import CapacityUnitEnum
from src.models.cdm.generated.base.math.financial_unit_enum import FinancialUnitEnum
from src.models.cdm.generated.base.math.weather_unit_enum import WeatherUnitEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
UnitType.model_rebuild()
