from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class PubliclyAvailableInformation(CdmModelBase):
    """"""
    standard_public_sources: bool = Field(None, description="If this element is specified and set to 'true', indicates that ISDA defined Standard Public Sources are applicable.")
    public_source: List[List] = Field(None, description="A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred. ISDA 2003 Term: Public Source.")
    specified_number: int = Field(None, description="The minimum number of the specified public information sources that must publish information that reasonably confirms that a credit event has occurred. The market convention is two. ISDA 2003 Term: Specified Number.")

# Import after class definition to avoid circular imports
PubliclyAvailableInformation.model_rebuild()
