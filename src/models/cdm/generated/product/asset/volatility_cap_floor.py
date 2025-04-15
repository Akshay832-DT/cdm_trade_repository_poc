from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class VolatilityCapFloor(CdmModelBase):
    """Contains volatility-based barriers. Volatility Cap needs to be specified in accordance with the ISDA 2011 Equity Derivatives Definitions."""
    applicable: bool = Field(description="Indicates whether the volatility cap is applicable in accordance with the ISDA 2011 Equity Derivatives Definitions. Setting the element 'applicable' to 'False' - means No Volatility Cap and no 'totalVolatilityCap' or 'volatilityCapFactor' should be provided. Setting the element 'applicable' to 'True' - means Volatility Cap election, then 'totalVolatilityCap' or 'volatilityCapFactor' should be provided, otherwise it defaults to volatilityCapFactor=2.5.")
    total_volatility_cap: float = Field(None, description="Volatility Cap Amount in accordance with the ISDA 2011 Equity Derivatives Definitions. This means the Volatility Cap Amount election is a number.")
    volatility_cap_factor: float = Field(None, description="Volatility Cap Amount in accordance with the ISDA 2011 Equity Derivatives Definitions. The Calculated VolCapAmt can be optionally provided.")

# Import after class definition to avoid circular imports
VolatilityCapFloor.model_rebuild()
