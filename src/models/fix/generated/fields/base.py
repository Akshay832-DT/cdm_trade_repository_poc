
from pydantic import BaseModel, Field

class FIXFieldBase(BaseModel):
    """Base class for FIX fields."""
    tag: str
    name: str
    type: str
    description: str = ""
    values: list = []
