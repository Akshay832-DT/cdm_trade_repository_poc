from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class RegionalGovernmentIssuerType(CdmModelBase):
    """Represents a class to allow specification of different type of Regional government collateral."""
    sovereign_recourse: bool = Field(description="Applies to regional governments, local authorities or municipals.  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.")

# Import after class definition to avoid circular imports
RegionalGovernmentIssuerType.model_rebuild()
