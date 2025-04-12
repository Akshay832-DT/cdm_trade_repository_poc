"""
FIX 4.4 RegistrationInstructions Message

This module contains the Pydantic model for the RegistrationInstructions message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from ..fields.common import *
from ...base import TradeModel
from ..components.parties import Parties
from ..components.rgstdistinstgrp import RgstDistInstGrp
from ..components.rgstdtlsgrp import RgstDtlsGrp


class RegistrationInstructions(TradeModel):
    """
    FIX 4.4 RegistrationInstructions Message
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
    MsgType: Literal["o"] = Field(alias='35')
    SenderCompID: str = Field(..., alias='49')
    TargetCompID: str = Field(..., alias='56')
    MsgSeqNum: int = Field(..., alias='34')
    SendingTime: datetime = Field(..., alias='52')
    
    # Message-specific fields
    RegistID: str = Field(None, description='', alias='513')
    RegistTransType: str = Field(None, description='', alias='514')
    RegistRefID: str = Field(None, description='', alias='508')
    ClOrdID: Optional[str] = Field(None, description='', alias='11')
    Account: Optional[str] = Field(None, description='', alias='1')
    AcctIDSource: Optional[int] = Field(None, description='', alias='660')
    RegistAcctType: Optional[str] = Field(None, description='', alias='493')
    TaxAdvantageType: Optional[int] = Field(None, description='', alias='495')
    OwnershipType: Optional[str] = Field(None, description='', alias='517')
    Parties: Optional[Parties] = None
    RgstDtlsGrp: Optional[RgstDtlsGrp] = None
    RgstDistInstGrp: Optional[RgstDistInstGrp] = None

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
