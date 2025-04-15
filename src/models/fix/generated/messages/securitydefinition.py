"""
FIX SecurityDefinition Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.instrumentextension import InstrumentExtensionComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
InstrumentExtensionComponent = ForwardRef('InstrumentExtensionComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class SecurityDefinitionMessage(FIXMessageBase):
    """SecurityDefinition Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SecurityDefinition"] = Field("SecurityDefinition", alias="35", description="Message Type")

    SecurityReqID: Optional[str] = Field(None, alias="320", description="")
    SecurityResponseID: Optional[str] = Field(None, alias="322", description="")
    SecurityResponseType: Optional[int] = Field(None, alias="323", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    ExpirationCycle: Optional[int] = Field(None, alias="827", description="")
    RoundLot: Optional[float] = Field(None, alias="561", description="")
    MinTradeVol: Optional[float] = Field(None, alias="562", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrumentExtension: ForwardRef('InstrumentExtensionComponent') = Field(None, description="InstrumentExtension Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")

    @model_validator(mode='after')
    def resolve_forward_refs(self) -> 'FIXMessageBase':
        """Resolve forward references."""
        for field_name, field_value in self.model_fields.items():
            if isinstance(field_value.annotation, ForwardRef):
                field_value.annotation = eval(field_value.annotation.__forward_arg__)
        return self

    def __str__(self) -> str:
        fields = []
        if self.MsgType is not None:
            fields.append(f"MsgType={self.MsgType}")
        if self.SecurityReqID is not None:
            fields.append(f"SecurityReqID={self.SecurityReqID}")
        if self.SecurityResponseID is not None:
            fields.append(f"SecurityResponseID={self.SecurityResponseID}")
        if self.SecurityResponseType is not None:
            fields.append(f"SecurityResponseType={self.SecurityResponseType}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.ExpirationCycle is not None:
            fields.append(f"ExpirationCycle={self.ExpirationCycle}")
        if self.RoundLot is not None:
            fields.append(f"RoundLot={self.RoundLot}")
        if self.MinTradeVol is not None:
            fields.append(f"MinTradeVol={self.MinTradeVol}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.InstrumentExtension is not None:
            fields.append(f"InstrumentExtension={self.InstrumentExtension}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
SecurityDefinitionMessage.model_rebuild()
