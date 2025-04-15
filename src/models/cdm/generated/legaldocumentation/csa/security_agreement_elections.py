from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class SecurityAgreementElections(CdmModelBase):
    """The set of elections which specify a Security Agremeent"""

# Import after class definition to avoid circular imports
SecurityAgreementElections.model_rebuild()
