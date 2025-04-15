"""
FIX PositionMaintenanceReport Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.instrmtleggrp import InstrmtLegGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.parties import PartiesComponent
    from ..components.positionamountdata import PositionAmountDataComponent
    from ..components.positionqty import PositionQtyComponent
    from ..components.trdgsesgrp import TrdgSesGrpComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
PositionAmountDataComponent = ForwardRef('PositionAmountDataComponent')
PositionQtyComponent = ForwardRef('PositionQtyComponent')
TrdgSesGrpComponent = ForwardRef('TrdgSesGrpComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class PositionMaintenanceReportMessage(FIXMessageBase):
    """PositionMaintenanceReport Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["PositionMaintenanceReport"] = Field("PositionMaintenanceReport", alias="35", description="Message Type")

    PosMaintRptID: Optional[str] = Field(None, alias="721", description="")
    PosTransType: Optional[int] = Field(None, alias="709", description="")
    PosReqID: Optional[str] = Field(None, alias="710", description="")
    PosMaintAction: Optional[int] = Field(None, alias="712", description="")
    OrigPosReqRefID: Optional[str] = Field(None, alias="713", description="")
    PosMaintStatus: Optional[int] = Field(None, alias="722", description="")
    PosMaintResult: Optional[int] = Field(None, alias="723", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    SettlSessID: Optional[str] = Field(None, alias="716", description="")
    SettlSessSubID: Optional[str] = Field(None, alias="717", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    AdjustmentType: Optional[int] = Field(None, alias="718", description="")
    ThresholdAmount: Optional[float] = Field(None, alias="834", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    TrdgSesGrp: ForwardRef('TrdgSesGrpComponent') = Field(None, description="TrdgSesGrp Component")
    PositionQty: ForwardRef('PositionQtyComponent') = Field(None, description="PositionQty Component")
    PositionAmountData: ForwardRef('PositionAmountDataComponent') = Field(None, description="PositionAmountData Component")

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
        if self.PosMaintRptID is not None:
            fields.append(f"PosMaintRptID={self.PosMaintRptID}")
        if self.PosTransType is not None:
            fields.append(f"PosTransType={self.PosTransType}")
        if self.PosReqID is not None:
            fields.append(f"PosReqID={self.PosReqID}")
        if self.PosMaintAction is not None:
            fields.append(f"PosMaintAction={self.PosMaintAction}")
        if self.OrigPosReqRefID is not None:
            fields.append(f"OrigPosReqRefID={self.OrigPosReqRefID}")
        if self.PosMaintStatus is not None:
            fields.append(f"PosMaintStatus={self.PosMaintStatus}")
        if self.PosMaintResult is not None:
            fields.append(f"PosMaintResult={self.PosMaintResult}")
        if self.ClearingBusinessDate is not None:
            fields.append(f"ClearingBusinessDate={self.ClearingBusinessDate}")
        if self.SettlSessID is not None:
            fields.append(f"SettlSessID={self.SettlSessID}")
        if self.SettlSessSubID is not None:
            fields.append(f"SettlSessSubID={self.SettlSessSubID}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.AdjustmentType is not None:
            fields.append(f"AdjustmentType={self.AdjustmentType}")
        if self.ThresholdAmount is not None:
            fields.append(f"ThresholdAmount={self.ThresholdAmount}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.InstrmtLegGrp is not None:
            fields.append(f"InstrmtLegGrp={self.InstrmtLegGrp}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.TrdgSesGrp is not None:
            fields.append(f"TrdgSesGrp={self.TrdgSesGrp}")
        if self.PositionQty is not None:
            fields.append(f"PositionQty={self.PositionQty}")
        if self.PositionAmountData is not None:
            fields.append(f"PositionAmountData={self.PositionAmountData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
PositionMaintenanceReportMessage.model_rebuild()
