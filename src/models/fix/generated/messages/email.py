"""
FIX 4.4 Email Message

This module contains the Pydantic model for the Email message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.instrmtgrp import InstrmtGrp
from ..components.instrmtleggrp import InstrmtLegGrp
from ..components.linesoftextgrp import LinesOfTextGrp
from ..components.routinggrp import RoutingGrp
from ..components.undinstrmtgrp import UndInstrmtGrp


class Email(TradeModel):
    """
    FIX 4.4 Email Message
    """
    model_config = ConfigDict(
        populate_by_name=True,
        validate_by_name=True,
        json_encoders={
            datetime: lambda v: v.isoformat(),
            date: lambda v: v.isoformat(),
            time: lambda v: v.isoformat()
        }
    )
    
    # Standard FIX header fields
    BeginString: Literal["FIX.4.4"] = Field(alias='8')
    BodyLength: Optional[int] = Field(None, alias='9')
    MsgType: Literal["C"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    EmailThreadID: str = Field(None, description='', alias='164')
    EmailType: str = Field(None, description='', alias='94')
    OrigTime: Optional[datetime] = Field(None, description='', alias='42')
    Subject: str = Field(None, description='', alias='147')
    EncodedSubjectLen: Optional[int] = Field(None, description='', alias='356')
    EncodedSubject: Optional[str] = Field(None, description='', alias='357')
    OrderID: Optional[str] = Field(None, description='', alias='37')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    RawDataLength: Optional[int] = Field(None, description='', alias='95')
    RawData: Optional[str] = Field(None, description='', alias='96')
    RoutingGrp: Optional[RoutingGrp] = None
    InstrmtGrp: Optional[InstrmtGrp] = None
    UndInstrmtGrp: Optional[UndInstrmtGrp] = None
    InstrmtLegGrp: Optional[InstrmtLegGrp] = None
    LinesOfTextGrp: LinesOfTextGrp = Field(..., description='LinesOfTextGrp component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"No{field_name[:-1]}"  # Remove 's' from plural
                if no_field in self.__fields__:
                    data[no_field] = len(value)
        
        return {k: v for k, v in data.items() if v is not None and (not isinstance(v, list) or v)}
