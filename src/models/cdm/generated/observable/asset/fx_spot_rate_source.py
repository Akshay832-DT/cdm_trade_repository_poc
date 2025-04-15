from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.observable.asset.information_source import InformationSource

class FxSpotRateSource(CdmModelBase):
    """A class defining the rate source and fixing time for an FX rate."""
    primary_source: ForwardRef("InformationSource") = Field(description="The primary source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.")
    secondary_source: ForwardRef("InformationSource") = Field(None, description="An alternative, or secondary, source for where the rate observation will occur. Will typically be either a page or a reference bank published rate.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.observable.asset.information_source import InformationSource
FxSpotRateSource.model_rebuild()
