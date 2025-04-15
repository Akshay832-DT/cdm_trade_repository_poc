"""
FIX SecurityStatus Message
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


class SecurityStatusMessage(FIXMessageBase):
    """SecurityStatus Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["SecurityStatus"] = Field("SecurityStatus", alias="35", description="Message Type")

    SecurityStatusReqID: Optional[str] = Field(None, alias="324", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    UnsolicitedIndicator: Optional[bool] = Field(None, alias="325", description="")
    SecurityTradingStatus: Optional[int] = Field(None, alias="326", description="")
    FinancialStatus: Optional[List[str]] = Field(None, alias="291", description="")
    CorporateAction: Optional[List[str]] = Field(None, alias="292", description="")
    HaltReasonChar: Optional[str] = Field(None, alias="327", description="")
    InViewOfCommon: Optional[bool] = Field(None, alias="328", description="")
    DueToRelated: Optional[bool] = Field(None, alias="329", description="")
    BuyVolume: Optional[float] = Field(None, alias="330", description="")
    SellVolume: Optional[float] = Field(None, alias="331", description="")
    HighPx: Optional[float] = Field(None, alias="332", description="")
    LowPx: Optional[float] = Field(None, alias="333", description="")
    LastPx: Optional[float] = Field(None, alias="31", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    Adjustment: Optional[int] = Field(None, alias="334", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
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
        if self.SecurityStatusReqID is not None:
            fields.append(f"SecurityStatusReqID={self.SecurityStatusReqID}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.UnsolicitedIndicator is not None:
            fields.append(f"UnsolicitedIndicator={self.UnsolicitedIndicator}")
        if self.SecurityTradingStatus is not None:
            fields.append(f"SecurityTradingStatus={self.SecurityTradingStatus}")
        if self.FinancialStatus is not None:
            fields.append(f"FinancialStatus={self.FinancialStatus}")
        if self.CorporateAction is not None:
            fields.append(f"CorporateAction={self.CorporateAction}")
        if self.HaltReasonChar is not None:
            fields.append(f"HaltReasonChar={self.HaltReasonChar}")
        if self.InViewOfCommon is not None:
            fields.append(f"InViewOfCommon={self.InViewOfCommon}")
        if self.DueToRelated is not None:
            fields.append(f"DueToRelated={self.DueToRelated}")
        if self.BuyVolume is not None:
            fields.append(f"BuyVolume={self.BuyVolume}")
        if self.SellVolume is not None:
            fields.append(f"SellVolume={self.SellVolume}")
        if self.HighPx is not None:
            fields.append(f"HighPx={self.HighPx}")
        if self.LowPx is not None:
            fields.append(f"LowPx={self.LowPx}")
        if self.LastPx is not None:
            fields.append(f"LastPx={self.LastPx}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.Adjustment is not None:
            fields.append(f"Adjustment={self.Adjustment}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
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
SecurityStatusMessage.model_rebuild()
