from datetime import datetime, date, time
from pydantic import BaseModel, ConfigDict

class FIXMessageBase(BaseModel):
    """FIX message base model."""
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
