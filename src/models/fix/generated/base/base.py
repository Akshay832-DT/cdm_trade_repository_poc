"""
FIX message base class.
"""

from typing import Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class FIXMessageBase(BaseModel):
    """
    Base class for FIX messages.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    # Standard FIX header fields
    BeginString: str = Field(..., alias="8")
    BodyLength: int = Field(..., alias="9")
    MsgType: str = Field(..., alias="35")
    SenderCompID: str = Field(..., alias="49")
    TargetCompID: str = Field(..., alias="56")
    MsgSeqNum: int = Field(..., alias="34")
    SendingTime: str = Field(..., alias="52")
    CheckSum: str = Field(..., alias="10")

    def to_dict(self) -> Dict[str, Any]:
        """Convert message to dictionary."""
        return self.model_dump(by_alias=True)

    def __str__(self) -> str:
        """String representation of message."""
        fields = []
        for name, value in self.model_dump(by_alias=True).items():
            if value is not None:
                fields.append(f"{name}={value}")
        return f"{self.__class__.__name__}({", ".join(fields)})"

class FIXComponentBase(BaseModel):
    """
    Base class for FIX components.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
    )

    def to_dict(self) -> Dict[str, Any]:
        """Convert component to dictionary."""
        return self.model_dump(by_alias=True)

    def __str__(self) -> str:
        """String representation of component."""
        fields = []
        for name, value in self.model_dump(by_alias=True).items():
            if value is not None:
                fields.append(f"{name}={value}")
        return f"{self.__class__.__name__}({", ".join(fields)})"
