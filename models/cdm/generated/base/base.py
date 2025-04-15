"""
Base classes for ISDA CDM models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Dict, Any, Optional, List, ForwardRef, TYPE_CHECKING, Union
from datetime import date, datetime, time

class CdmModelBase(BaseModel):
    """Base class for all CDM models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra='forbid'
    )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert model to a dictionary."""
        return self.model_dump(exclude_none=True)
    
    def __str__(self) -> str:
        """String representation of the model."""
        fields = []
        for field_name, field_value in self.model_dump().items():
            if field_value is not None:
                fields.append(f"{field_name}={field_value}")
        return f"{self.__class__.__name__}({', '.join(fields)})"

class CdmProductBase(CdmModelBase):
    """Base class for CDM products."""
    pass

class CdmEventBase(CdmModelBase):
    """Base class for CDM events."""
    pass
