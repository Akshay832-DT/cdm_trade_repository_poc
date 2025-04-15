"""
FIX Quote Message
"""
from ..fields.types import *
from .base import FIXMessageBase
from datetime import datetime, date, time
from pydantic import Field, ConfigDict, model_validator
from typing import List, Optional, Dict, Any, Union, ForwardRef, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from ..components.financingdetails import FinancingDetailsComponent
    from ..components.instrument import InstrumentComponent
    from ..components.legquotgrp import LegQuotGrpComponent
    from ..components.orderqtydata import OrderQtyDataComponent
    from ..components.parties import PartiesComponent
    from ..components.quotqualgrp import QuotQualGrpComponent
    from ..components.spreadorbenchmarkcurvedata import SpreadOrBenchmarkCurveDataComponent
    from ..components.stipulations import StipulationsComponent
    from ..components.undinstrmtgrp import UndInstrmtGrpComponent
    from ..components.yielddata import YieldDataComponent


# Forward references for components to avoid circular imports
FinancingDetailsComponent = ForwardRef('FinancingDetailsComponent')
InstrumentComponent = ForwardRef('InstrumentComponent')
LegQuotGrpComponent = ForwardRef('LegQuotGrpComponent')
OrderQtyDataComponent = ForwardRef('OrderQtyDataComponent')
PartiesComponent = ForwardRef('PartiesComponent')
QuotQualGrpComponent = ForwardRef('QuotQualGrpComponent')
SpreadOrBenchmarkCurveDataComponent = ForwardRef('SpreadOrBenchmarkCurveDataComponent')
StipulationsComponent = ForwardRef('StipulationsComponent')
UndInstrmtGrpComponent = ForwardRef('UndInstrmtGrpComponent')
YieldDataComponent = ForwardRef('YieldDataComponent')


class QuoteMessage(FIXMessageBase):
    """Quote Message"""

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        json_encoders={
            datetime: lambda v: v.isoformat() if v else None,
            date: lambda v: v.isoformat() if v else None,
            time: lambda v: v.isoformat() if v else None
        }
    )

    MsgType: Literal["Quote"] = Field("Quote", alias="35", description="Message Type")

    QuoteReqID: Optional[str] = Field(None, alias="131", description="")
    QuoteID: Optional[str] = Field(None, alias="117", description="")
    QuoteRespID: Optional[str] = Field(None, alias="693", description="")
    QuoteType: Optional[int] = Field(None, alias="537", description="")
    QuoteResponseLevel: Optional[int] = Field(None, alias="301", description="")
    TradingSessionID: Optional[str] = Field(None, alias="336", description="")
    TradingSessionSubID: Optional[str] = Field(None, alias="625", description="")
    Side: Optional[str] = Field(None, alias="54", description="")
    SettlType: Optional[str] = Field(None, alias="63", description="")
    SettlDate: Optional[date] = Field(None, alias="64", description="")
    SettlDate2: Optional[date] = Field(None, alias="193", description="")
    OrderQty2: Optional[float] = Field(None, alias="192", description="")
    Currency: Optional[str] = Field(None, alias="15", description="")
    Account: Optional[str] = Field(None, alias="1", description="")
    AcctIDSource: Optional[int] = Field(None, alias="660", description="")
    AccountType: Optional[int] = Field(None, alias="581", description="")
    BidPx: Optional[float] = Field(None, alias="132", description="")
    OfferPx: Optional[float] = Field(None, alias="133", description="")
    MktBidPx: Optional[float] = Field(None, alias="645", description="")
    MktOfferPx: Optional[float] = Field(None, alias="646", description="")
    MinBidSize: Optional[float] = Field(None, alias="647", description="")
    BidSize: Optional[float] = Field(None, alias="134", description="")
    MinOfferSize: Optional[float] = Field(None, alias="648", description="")
    OfferSize: Optional[float] = Field(None, alias="135", description="")
    ValidUntilTime: Optional[datetime] = Field(None, alias="62", description="")
    BidSpotRate: Optional[float] = Field(None, alias="188", description="")
    OfferSpotRate: Optional[float] = Field(None, alias="190", description="")
    BidForwardPoints: Optional[float] = Field(None, alias="189", description="")
    OfferForwardPoints: Optional[float] = Field(None, alias="191", description="")
    MidPx: Optional[float] = Field(None, alias="631", description="")
    BidYield: Optional[float] = Field(None, alias="632", description="")
    MidYield: Optional[float] = Field(None, alias="633", description="")
    OfferYield: Optional[float] = Field(None, alias="634", description="")
    TransactTime: Optional[datetime] = Field(None, alias="60", description="")
    OrdType: Optional[str] = Field(None, alias="40", description="")
    BidForwardPoints2: Optional[float] = Field(None, alias="642", description="")
    OfferForwardPoints2: Optional[float] = Field(None, alias="643", description="")
    SettlCurrBidFxRate: Optional[float] = Field(None, alias="656", description="")
    SettlCurrOfferFxRate: Optional[float] = Field(None, alias="657", description="")
    SettlCurrFxRateCalc: Optional[str] = Field(None, alias="156", description="")
    CommType: Optional[str] = Field(None, alias="13", description="")
    Commission: Optional[float] = Field(None, alias="12", description="")
    CustOrderCapacity: Optional[int] = Field(None, alias="582", description="")
    ExDestination: Optional[str] = Field(None, alias="100", description="")
    OrderCapacity: Optional[str] = Field(None, alias="528", description="")
    PriceType: Optional[int] = Field(None, alias="423", description="")
    Text: Optional[str] = Field(None, alias="58", description="")
    EncodedTextLen: Optional[int] = Field(None, alias="354", description="")
    EncodedText: Optional[str] = Field(None, alias="355", description="")
    QuotQualGrp: ForwardRef('QuotQualGrpComponent') = Field(None, description="QuotQualGrp Component")
    Parties: ForwardRef('PartiesComponent') = Field(None, description="Parties Component")
    Instrument: ForwardRef('InstrumentComponent') = Field(None, description="Instrument Component")
    FinancingDetails: ForwardRef('FinancingDetailsComponent') = Field(None, description="FinancingDetails Component")
    UndInstrmtGrp: ForwardRef('UndInstrmtGrpComponent') = Field(None, description="UndInstrmtGrp Component")
    OrderQtyData: ForwardRef('OrderQtyDataComponent') = Field(None, description="OrderQtyData Component")
    Stipulations: ForwardRef('StipulationsComponent') = Field(None, description="Stipulations Component")
    LegQuotGrp: ForwardRef('LegQuotGrpComponent') = Field(None, description="LegQuotGrp Component")
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
        if self.QuoteReqID is not None:
            fields.append(f"QuoteReqID={self.QuoteReqID}")
        if self.QuoteID is not None:
            fields.append(f"QuoteID={self.QuoteID}")
        if self.QuoteRespID is not None:
            fields.append(f"QuoteRespID={self.QuoteRespID}")
        if self.QuoteType is not None:
            fields.append(f"QuoteType={self.QuoteType}")
        if self.QuoteResponseLevel is not None:
            fields.append(f"QuoteResponseLevel={self.QuoteResponseLevel}")
        if self.TradingSessionID is not None:
            fields.append(f"TradingSessionID={self.TradingSessionID}")
        if self.TradingSessionSubID is not None:
            fields.append(f"TradingSessionSubID={self.TradingSessionSubID}")
        if self.Side is not None:
            fields.append(f"Side={self.Side}")
        if self.SettlType is not None:
            fields.append(f"SettlType={self.SettlType}")
        if self.SettlDate is not None:
            fields.append(f"SettlDate={self.SettlDate}")
        if self.SettlDate2 is not None:
            fields.append(f"SettlDate2={self.SettlDate2}")
        if self.OrderQty2 is not None:
            fields.append(f"OrderQty2={self.OrderQty2}")
        if self.Currency is not None:
            fields.append(f"Currency={self.Currency}")
        if self.Account is not None:
            fields.append(f"Account={self.Account}")
        if self.AcctIDSource is not None:
            fields.append(f"AcctIDSource={self.AcctIDSource}")
        if self.AccountType is not None:
            fields.append(f"AccountType={self.AccountType}")
        if self.BidPx is not None:
            fields.append(f"BidPx={self.BidPx}")
        if self.OfferPx is not None:
            fields.append(f"OfferPx={self.OfferPx}")
        if self.MktBidPx is not None:
            fields.append(f"MktBidPx={self.MktBidPx}")
        if self.MktOfferPx is not None:
            fields.append(f"MktOfferPx={self.MktOfferPx}")
        if self.MinBidSize is not None:
            fields.append(f"MinBidSize={self.MinBidSize}")
        if self.BidSize is not None:
            fields.append(f"BidSize={self.BidSize}")
        if self.MinOfferSize is not None:
            fields.append(f"MinOfferSize={self.MinOfferSize}")
        if self.OfferSize is not None:
            fields.append(f"OfferSize={self.OfferSize}")
        if self.ValidUntilTime is not None:
            fields.append(f"ValidUntilTime={self.ValidUntilTime}")
        if self.BidSpotRate is not None:
            fields.append(f"BidSpotRate={self.BidSpotRate}")
        if self.OfferSpotRate is not None:
            fields.append(f"OfferSpotRate={self.OfferSpotRate}")
        if self.BidForwardPoints is not None:
            fields.append(f"BidForwardPoints={self.BidForwardPoints}")
        if self.OfferForwardPoints is not None:
            fields.append(f"OfferForwardPoints={self.OfferForwardPoints}")
        if self.MidPx is not None:
            fields.append(f"MidPx={self.MidPx}")
        if self.BidYield is not None:
            fields.append(f"BidYield={self.BidYield}")
        if self.MidYield is not None:
            fields.append(f"MidYield={self.MidYield}")
        if self.OfferYield is not None:
            fields.append(f"OfferYield={self.OfferYield}")
        if self.TransactTime is not None:
            fields.append(f"TransactTime={self.TransactTime}")
        if self.OrdType is not None:
            fields.append(f"OrdType={self.OrdType}")
        if self.BidForwardPoints2 is not None:
            fields.append(f"BidForwardPoints2={self.BidForwardPoints2}")
        if self.OfferForwardPoints2 is not None:
            fields.append(f"OfferForwardPoints2={self.OfferForwardPoints2}")
        if self.SettlCurrBidFxRate is not None:
            fields.append(f"SettlCurrBidFxRate={self.SettlCurrBidFxRate}")
        if self.SettlCurrOfferFxRate is not None:
            fields.append(f"SettlCurrOfferFxRate={self.SettlCurrOfferFxRate}")
        if self.SettlCurrFxRateCalc is not None:
            fields.append(f"SettlCurrFxRateCalc={self.SettlCurrFxRateCalc}")
        if self.CommType is not None:
            fields.append(f"CommType={self.CommType}")
        if self.Commission is not None:
            fields.append(f"Commission={self.Commission}")
        if self.CustOrderCapacity is not None:
            fields.append(f"CustOrderCapacity={self.CustOrderCapacity}")
        if self.ExDestination is not None:
            fields.append(f"ExDestination={self.ExDestination}")
        if self.OrderCapacity is not None:
            fields.append(f"OrderCapacity={self.OrderCapacity}")
        if self.PriceType is not None:
            fields.append(f"PriceType={self.PriceType}")
        if self.Text is not None:
            fields.append(f"Text={self.Text}")
        if self.EncodedTextLen is not None:
            fields.append(f"EncodedTextLen={self.EncodedTextLen}")
        if self.EncodedText is not None:
            fields.append(f"EncodedText={self.EncodedText}")
        if self.QuotQualGrp is not None:
            fields.append(f"QuotQualGrp={self.QuotQualGrp}")
        if self.Parties is not None:
            fields.append(f"Parties={self.Parties}")
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
        if self.LegQuotGrp is not None:
            fields.append(f"LegQuotGrp={self.LegQuotGrp}")
        if self.SpreadOrBenchmarkCurveData is not None:
            fields.append(f"SpreadOrBenchmarkCurveData={self.SpreadOrBenchmarkCurveData}")
        if self.YieldData is not None:
            fields.append(f"YieldData={self.YieldData}")
        return f"{self.__class__.__name__}({', '.join(fields)})"


# Rebuild model to resolve forward references
QuoteMessage.model_rebuild()
