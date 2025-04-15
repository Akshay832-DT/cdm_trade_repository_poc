"""FIX Field Model"""
from typing import Optional, List, Dict, Any, Union, Literal
from pydantic import Field, ConfigDict
from datetime import datetime, date, time
from decimal import Decimal
from ..base.base import FIXFieldBase

class NoNested3PartyIDsField(FIXFieldBase):
    """FIX NoNested3PartyIDs Field"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    value: Optional[int] = Field(None, alias='948', description='')

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(value={self.value})"
