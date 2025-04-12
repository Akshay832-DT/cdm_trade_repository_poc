"""
FIX 4.4 OrderCancelRequest Message

This module contains the Pydantic model for the OrderCancelRequest message.
"""
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict, Any, Literal
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.base import FIXMessageBase
from src.models.fix.generated.fields.common import *
from src.models.fix.generated.components.financingdetails import FinancingDetails
from src.models.fix.generated.components.instrument import Instrument
from src.models.fix.generated.components.orderqtydata import OrderQtyData
from src.models.fix.generated.components.parties import Parties
from src.models.fix.generated.components.undinstrmtgrp import UndInstrmtGrp


class OrderCancelRequest(FIXMessageBase):
    """
    FIX 4.4 OrderCancelRequest Message
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
    
    # Set the message type for this message
    msgType: Literal["F"] = Field("F", alias='35')
    
    # Message-specific fields
    origClOrdID: Optional[str] = Field(None, description='', alias='41')
    orderID: Optional[str] = Field(None, description='', alias='37')
    clOrdID: Optional[str] = Field(None, description='', alias='11')
    secondaryClOrdID: Optional[str] = Field(None, description='', alias='526')
    clOrdLinkID: Optional[str] = Field(None, description='', alias='583')
    listID: Optional[str] = Field(None, description='', alias='66')
    origOrdModTime: Optional[datetime] = Field(None, description='', alias='586')
    account: Optional[str] = Field(None, description='', alias='1')
    acctIDSource: Optional[int] = Field(None, description='', alias='660')
    accountType: Optional[int] = Field(None, description='', alias='581')
    side: Optional[str] = Field(None, description='', alias='54')
    transactTime: Optional[datetime] = Field(None, description='', alias='60')
    complianceID: Optional[str] = Field(None, description='', alias='376')
    text: Optional[str] = Field(None, description='', alias='58')
    encodedTextLen: Optional[int] = Field(None, description='', alias='354')
    encodedText: Optional[str] = Field(None, description='', alias='355')
    parties: Optional[Parties] = Field(None, description='Parties component')
    instrument: Optional[Instrument] = Field(None, description='Instrument component')
    financingDetails: Optional[FinancingDetails] = Field(None, description='FinancingDetails component')
    undInstrmtGrp: Optional[UndInstrmtGrp] = Field(None, description='UndInstrmtGrp component')
    orderQtyData: Optional[OrderQtyData] = Field(None, description='OrderQtyData component')

    def model_dump(self, **kwargs) -> Dict[str, Any]:
        """Override model_dump to handle nested components"""
        kwargs.setdefault('by_alias', True)
        data = super().model_dump(**kwargs)
        
        # Handle repeating components
        for field_name, value in data.items():
            if isinstance(value, list):
                # Set the No* field based on list length
                no_field = f"no{field_name}"  # Convert to camelCase
                if hasattr(self, no_field):
                    setattr(self, no_field, len(value))
        
        return data
