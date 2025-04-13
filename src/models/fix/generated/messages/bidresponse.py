from typing import Optional, List
from datetime import datetime, date, time
from pydantic import BaseModel, Field, ConfigDict
from src.models.fix.generated.components.bidcomprspgrp import BidCompRspGrp

class BidResponse(BaseModel):
    """FIX message model."""
    
    model_config = ConfigDict(
        json_encoders={
            datetime: str,
            date: str,
            time: str
        }
    )

    beginstring: str = Field(..., description='', alias='8')
    bodylength: int = Field(..., description='', alias='9')
    msgtype: str = Field(..., description='', alias='35')
    sendercompid: str = Field(..., description='', alias='49')
    targetcompid: str = Field(..., description='', alias='56')
    msgseqnum: int = Field(..., description='', alias='34')
    sendingtime: datetime = Field(..., description='', alias='52')
    bidid: Optional[str] = Field(None, description='', alias='390')
    clientbidid: Optional[str] = Field(None, description='', alias='391')
    bidcomprspgrp: BidCompRspGrp = Field(..., description='BidCompRspGrp component')

