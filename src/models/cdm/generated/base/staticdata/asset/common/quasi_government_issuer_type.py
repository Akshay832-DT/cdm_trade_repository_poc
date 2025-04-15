from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class QuasiGovernmentIssuerType(CdmModelBase):
    """Represents a class to allow specification of different types of Quasi Government collateral."""
    sovereign_entity: bool = Field(description="True if sovereign entity (e.g. not separate legal personality from sovereign) or false if non-sovereign entity (e.g. separate legal personality from sovereign).")
    sovereign_recourse: bool = Field(None, description="Applies to non-sovereign entity (e.g. separate legal personality from sovereign).  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.")

# Import after class definition to avoid circular imports
QuasiGovernmentIssuerType.model_rebuild()
