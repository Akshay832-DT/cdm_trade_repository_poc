"""
FIX AssignmentReport Message
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
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent


# Forward references for components to avoid circular imports
InstrmtLegGrpComponent = ForwardRef('InstrmtLegGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
PartiesComponent = ForwardRef('PartiesComponent')
PositionAmountDataComponent = ForwardRef('PositionAmountDataComponent')
PositionQtyComponent = ForwardRef('PositionQtyComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')


class AssignmentReportMessage(FIXMessageBase):
    """AssignmentReport Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["AssignmentReport"] = Field("AssignmentReport", alias="35", description="Message Type")

    AsgnRptID: Optional[str] = Field(None, alias="833", description="")
    TotNumAssignmentReports: Optional[int] = Field(None, alias="832", description="")
    LastRptRequested: Optional[bool] = Field(None, alias="912", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    ThresholdAmount: Optional[float] = Field(None, alias="834", description="")
    SettlPrice: Optional[float] = Field(None, alias="730", description="")
    SettlPriceType: Optional[int] = Field(None, alias="731", description="")
    UnderlyingSettlPrice: Optional[float] = Field(None, alias="732", description="")
    ExpireDate: Optional[date] = Field(None, alias="432", description="")
    AssignmentMethod: Optional[str] = Field(None, alias="744", description="")
    AssignmentUnit: Optional[float] = Field(None, alias="745", description="")
    OpenInterest: Optional[float] = Field(None, alias="746", description="")
    ExerciseMethod: Optional[str] = Field(None, alias="747", description="")
    SettlSessID: Optional[str] = Field(None, alias="716", description="")
    SettlSessSubID: Optional[str] = Field(None, alias="717", description="")
    ClearingBusinessDate: Optional[date] = Field(None, alias="715", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    InstrmtLegGrp: ForwardRef('InstrmtLegGrpComponent') = Field(None, description="InstrmtLegGrp Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
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
        if self.AsgnRptID is not None:
            fields.append(f"AsgnRptID={self.AsgnRptID}")
        if self.TotNumAssignmentReports is not None:
            fields.append(f"TotNumAssignmentReports={self.TotNumAssignmentReports}")
        if self.LastRptRequested is not None:
            fields.append(f"LastRptRequested={self.LastRptRequested}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.ThresholdAmount is not None:
            fields.append(f"ThresholdAmount={self.ThresholdAmount}")
        if self.SettlPrice is not None:
            fields.append(f"SettlPrice={self.SettlPrice}")
        if self.SettlPriceType is not None:
            fields.append(f"SettlPriceType={self.SettlPriceType}")
        if self.UnderlyingSettlPrice is not None:
            fields.append(f"UnderlyingSettlPrice={self.UnderlyingSettlPrice}")
        if self.ExpireDate is not None:
            fields.append(f"ExpireDate={self.ExpireDate}")
        if self.AssignmentMethod is not None:
            fields.append(f"AssignmentMethod={self.AssignmentMethod}")
        if self.AssignmentUnit is not None:
            fields.append(f"AssignmentUnit={self.AssignmentUnit}")
        if self.OpenInterest is not None:
            fields.append(f"OpenInterest={self.OpenInterest}")
        if self.ExerciseMethod is not None:
            fields.append(f"ExerciseMethod={self.ExerciseMethod}")
        if self.SettlSessID is not None:
            fields.append(f"SettlSessID={self.SettlSessID}")
        if self.SettlSessSubID is not None:
            fields.append(f"SettlSessSubID={self.SettlSessSubID}")
        if self.ClearingBusinessDate is not None:
            fields.append(f"ClearingBusinessDate={self.ClearingBusinessDate}")
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
        if self.PositionQty is not None:
            fields.append(f"PositionQty={self.PositionQty}")
        if self.PositionAmountData is not None:
            fields.append(f"PositionAmountData={self.PositionAmountData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
AssignmentReportMessage.model_rebuild()
