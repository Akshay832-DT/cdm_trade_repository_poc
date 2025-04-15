"""
FIX PositionReport Message
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
    from ..components.posundinstrmtgrp import PosUndInstrmtGrpComponent
    from ..components.positionamountdata import PositionAmountDataComponent
    from ..components.positionqty import PositionQtyComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
PosUndInstrmtGrpComponent = ForwardRef('PosUndInstrmtGrpComponent')
PositionAmountDataComponent = ForwardRef('PositionAmountDataComponent')
PositionQtyComponent = ForwardRef('PositionQtyComponent')


class PositionReportMessage(FIXMessageBase):
    """PositionReport Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["PositionReport"] = Field("PositionReport", alias="35", description="Message Type")

    PosMaintRptID: Optional[str] = Field(None, alias="721", description="")
    PosReqID: Optional[str] = Field(None, alias="710", description="")
    PosReqType: Optional[int] = Field(None, alias="724", description="")
    SubscriptionRequestType: Optional[str] = Field(None, alias="263", description="")
    TotalNumPosReports: Optional[int] = Field(None, alias="727", description="")
    UnsolicitedIndicator: Optional[bool] = Field(None, alias="325", description="")
    PosReqResult: Optional[int] = Field(None, alias="728", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    SettlSessID: Optional[str] = Field(None, alias="716", description="")
    SettlSessSubID: Optional[str] = Field(None, alias="717", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    SettlPrice: Optional[float] = Field(None, alias="730", description="")
    SettlPriceType: Optional[int] = Field(None, alias="731", description="")
    PriorSettlPrice: Optional[float] = Field(None, alias="734", description="")
    RegistStatus: Optional[str] = Field(None, alias="506", description="")
    DeliveryDate: Optional[date] = Field(None, alias="743", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    PosUndInstrmtGrp: ForwardRef('PosUndInstrmtGrpComponent') = Field(None, description="PosUndInstrmtGrp Component")
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
        if self.PosReqID is not None:
            fields.append(f"PosReqID={self.PosReqID}")
        if self.PosReqType is not None:
            fields.append(f"PosReqType={self.PosReqType}")
        if self.SubscriptionRequestType is not None:
            fields.append(f"SubscriptionRequestType={self.SubscriptionRequestType}")
        if self.TotalNumPosReports is not None:
            fields.append(f"TotalNumPosReports={self.TotalNumPosReports}")
        if self.UnsolicitedIndicator is not None:
            fields.append(f"UnsolicitedIndicator={self.UnsolicitedIndicator}")
        if self.PosReqResult is not None:
            fields.append(f"PosReqResult={self.PosReqResult}")
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
        if self.SettlPrice is not None:
            fields.append(f"SettlPrice={self.SettlPrice}")
        if self.SettlPriceType is not None:
            fields.append(f"SettlPriceType={self.SettlPriceType}")
        if self.PriorSettlPrice is not None:
            fields.append(f"PriorSettlPrice={self.PriorSettlPrice}")
        if self.RegistStatus is not None:
            fields.append(f"RegistStatus={self.RegistStatus}")
        if self.DeliveryDate is not None:
            fields.append(f"DeliveryDate={self.DeliveryDate}")
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
        if self.PosUndInstrmtGrp is not None:
            fields.append(f"PosUndInstrmtGrp={self.PosUndInstrmtGrp}")
        if self.PositionQty is not None:
            fields.append(f"PositionQty={self.PositionQty}")
        if self.PositionAmountData is not None:
            fields.append(f"PositionAmountData={self.PositionAmountData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
PositionReportMessage.model_rebuild()
