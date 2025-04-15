from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class HaircutIndicatorEnum(CdmModelBase):
    """Represents the enumeration indicators to specify if an asset or group of assets valuation is based on any valuation treatment haircut."""
    # Enum values
    PostHaircut: ClassVar[str] = "PostHaircut"
    PreHaircut: ClassVar[str] = "PreHaircut"


# Import after class definition to avoid circular imports
HaircutIndicatorEnum.model_rebuild()
