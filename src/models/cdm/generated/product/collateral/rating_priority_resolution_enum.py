from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RatingPriorityResolutionEnum(CdmModelBase):
    """Represents an enumeration list to identify which Collateral Criteria type should have priority over others. If set to 'Issuer', the rating in the Issuer Criteria has priority or is used if there is no Asset criteria. If set to 'Asset', the rating in the Asset Criteria has priority or is used if there is no Issuer rating."""
    # Enum values
    Asset: ClassVar[str] = "Asset"
    Average: ClassVar[str] = "Average"
    Highest: ClassVar[str] = "Highest"
    Issuer: ClassVar[str] = "Issuer"
    Lowest: ClassVar[str] = "Lowest"


# Import after class definition to avoid circular imports
RatingPriorityResolutionEnum.model_rebuild()
