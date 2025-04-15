"""
FIX IOI Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.ioiqualgrp import IOIQualGrpComponent
    from ..components.instrmtlegioigrp import InstrmtLegIOIGrpComponent
    from ..components.instrument import InstrumentComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.routinggrp import RoutingGrpComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
IOIQualGrpComponent = ForwardRef('IOIQualGrpComponent')
InstrmtLegIOIGrpComponent = ForwardRef('InstrmtLegIOIGrpComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
RoutingGrpComponent = ForwardRef('RoutingGrpComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class IOIMessage(FIXMessageBase):
    """IOI Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["IOI"] = Field("IOI", alias="35", description="Message Type")

    IOIID: Optional[str] = Field(None, alias="23", description="")
    IOITransType: Optional[str] = Field(None, alias="28", description="")
    IOIRefID: Optional[str] = Field(None, alias="26", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    QtyType: Optional[int] = Field(None, alias="854", description="")
    IOIQty: Optional[str] = Field(None, alias="27", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    Price: Optional[float] = Field(None, alias="44", description="")
    ValidUntilTime: Optional[datetime] = Field(None, alias="62", description="")
    IOIQltyInd: Optional[str] = Field(None, alias="25", description="")
    IOINaturalFlag: Optional[bool] = Field(None, alias="130", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    URLLink: Optional[str] = Field(None, alias="149", description="")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    InstrmtLegIOIGrp: ForwardRef('InstrmtLegIOIGrpComponent') = Field(None, description="InstrmtLegIOIGrp Component")
    IOIQualGrp: ForwardRef('IOIQualGrpComponent') = Field(None, description="IOIQualGrp Component")
    RoutingGrp: ForwardRef('RoutingGrpComponent') = Field(None, description="RoutingGrp Component")
    SpreadOrBenchmarkCurveData: ForwardRef('SpreadOrBenchmarkCurveDataComponent') = Field(None, description="SpreadOrBenchmarkCurveData Component")
    YieldData: ForwardRef('YieldDataComponent') = Field(None, description="YieldData Component")

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
        if self.IOIID is not None:
            fields.append(f"IOIID={self.IOIID}")
        if self.IOITransType is not None:
            fields.append(f"IOITransType={self.IOITransType}")
        if self.IOIRefID is not None:
            fields.append(f"IOIRefID={self.IOIRefID}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.QtyType is not None:
            fields.append(f"QtyType={self.QtyType}")
        if self.IOIQty is not None:
            fields.append(f"IOIQty={self.IOIQty}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.Price is not None:
            fields.append(f"Price={self.Price}")
        if self.ValidUntilTime is not None:
            fields.append(f"ValidUntilTime={self.ValidUntilTime}")
        if self.IOIQltyInd is not None:
            fields.append(f"IOIQltyInd={self.IOIQltyInd}")
        if self.IOINaturalFlag is not None:
            fields.append(f"IOINaturalFlag={self.IOINaturalFlag}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.URLLink is not None:
            fields.append(f"URLLink={self.URLLink}")
        if self.Instrument is not None:
            fields.append(f"Instrument={self.Instrument}")
        if self.FinancingDetails is not None:
            fields.append(f"FinancingDetails={self.FinancingDetails}")
        if self.UndInstrmtGrp is not None:
            fields.append(f"UndInstrmtGrp={self.UndInstrmtGrp}")
        if self.OrderQtyData is not None:
            fields.append(f"OrderQtyData={self.OrderQtyData}")
        if self.Stipulations is not None:
            fields.append(f"Stipulations={self.Stipulations}")
        if self.InstrmtLegIOIGrp is not None:
            fields.append(f"InstrmtLegIOIGrp={self.InstrmtLegIOIGrp}")
        if self.IOIQualGrp is not None:
            fields.append(f"IOIQualGrp={self.IOIQualGrp}")
        if self.RoutingGrp is not None:
            fields.append(f"RoutingGrp={self.RoutingGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
IOIMessage.model_rebuild()
