"""
Base classes for FpML models.
"""
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List, ForwardRef, TYPE_CHECKING
from datetime import date, datetime, time

class FpMLModelBase(BaseModel):
    """Base class for all FpML models."""
    class Config:
        populate_by_field_name = True
        validate_assignment = True
        extra = 'forbid'
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return self.dict()
    
    def __str__(self) -> str:
        """Convert the model to a string."""
        fields = []
        for field_name, field_value in self.dict().items():
            if field_value is not None:
                fields.append(f"{field_name}={field_value}")
        return f"{self.__class__.__name__}({', '.join(fields)})"

class FpMLTradeBase(FpMLModelBase):
    """Base class for FpML trades."""
    pass

class FpMLComponentBase(FpMLModelBase):
    """Base class for FpML components."""
    pass

class FpMLMessageBase(FpMLModelBase):
    """Base class for FpML messages."""
    pass
