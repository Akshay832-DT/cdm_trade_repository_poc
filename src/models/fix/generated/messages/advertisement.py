"""
FIX Advertisement Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class AdvertisementMessage(FIXMessageBase):
    """Advertisement Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Advertisement"] = Field("Advertisement", alias="35", description="Message Type")

    AdvId: Optional[str] = Field(None, alias="2", description="")
    AdvTransType: Optional[str] = Field(None, alias="5", description="")
    AdvRefID: Optional[str] = Field(None, alias="3", description="")
    AdvSide: Optional[str] = Field(None, alias="4", description="")
    Quantity: Optional[float] = Field(None, alias="53", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    TradeDate: Optional[date] = Field(None, alias="75", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    URLLink: Optional[str] = Field(None, alias="149", description="")
    LastMkt: Optional[str] = Field(None, alias="30", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")

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
        if self.AdvId is not None:
            fields.append(f"AdvId={self.AdvId}")
        if self.AdvTransType is not None:
            fields.append(f"AdvTransType={self.AdvTransType}")
        if self.AdvRefID is not None:
            fields.append(f"AdvRefID={self.AdvRefID}")
        if self.AdvSide is not None:
            fields.append(f"AdvSide={self.AdvSide}")
        if self.Quantity is not None:
            fields.append(f"Quantity={self.Quantity}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.Price is not None:
            fields.append(f"Price={self.Price}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.TradeDate is not None:
            fields.append(f"TradeDate={self.TradeDate}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.URLLink is not None:
            fields.append(f"URLLink={self.URLLink}")
        if self.LastMkt is not None:
            fields.append(f"LastMkt={self.LastMkt}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
AdvertisementMessage.model_rebuild()
