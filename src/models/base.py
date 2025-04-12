from pydantic import BaseModel, ConfigDict
from typing import Dict, Any
from abc import ABC, abstractmethod
from datetime import datetime, date

class TradeModel(BaseModel):
    """Base model for all trade-related models"""
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=None,  # Allow explicit aliases
        validate_by_name=True,  # Allow population by field name
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat()
        }
    )

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """
        Convert the model to a dictionary, handling nested components.
        """
        # Ensure by_alias is True by default
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        return {k: v for k, v in data.items() if v is not None}

class BaseParser(ABC):
    @abstractmethod
    async def parse(self, message: str) -> TradeModel:
        pass

    @abstractmethod
    async def validate(self, message: str) -> bool:
        pass 