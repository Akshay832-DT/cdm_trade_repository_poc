from pydantic import BaseModel
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