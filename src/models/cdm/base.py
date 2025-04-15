"""
Base class for CDM models.
"""
from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any


class TradeModel(BaseModel):
    """Base class for all CDM trade models."""
    
    def __init__(self, **data):
        super().__init__(**data)
    
    def model_dump(self) -> Dict[str, Any]:
        """Convert the model to a dictionary representation."""
        return self.dict()
    
    def to_json(self) -> str:
        """Convert the model to a JSON string."""
        return self.json()
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {} 

class CdmModelBase(BaseModel):
    """Base class for all CDM models."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        extra='forbid',
        alias_generator=None,
        validate_default=True
    )

    @classmethod
    def model_rebuild(cls) -> None:
        """Rebuild the model to handle forward references."""
        cls.model_rebuild = lambda: None  # type: ignore
        return None 