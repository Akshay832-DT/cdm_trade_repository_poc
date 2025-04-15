"""
Base classes for FIX field models.
"""
from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List, Any

class FIXFieldBase(BaseModel):
    """Base class for all FIX field models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True
    )
    
    tag: str
    name: str
    type: str
    description: str = ""
