from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ConstituentWeight(CdmModelBase):
    """A class describing the weight of each of the underlier constituent within the basket, either in absolute or relative terms."""
    open_units: float = Field(None, description="The number of units (index or securities) that constitute the underlier of the swap. In the case of a basket swap, this element is used to reference both the number of basket units, and the number of each asset components of the basket when these are expressed in absolute terms.")
    basket_percentage: float = Field(None, description="The relative weight of each respective basket constituent, expressed in percentage. A basket percentage of 5% would be represented as 0.05.")

# Import after class definition to avoid circular imports
ConstituentWeight.model_rebuild()
