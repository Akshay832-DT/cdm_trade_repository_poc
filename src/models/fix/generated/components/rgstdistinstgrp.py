"""
FIX Component Model - RgstDistInstGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoDistribInstsGroup(FIXComponentBase):

    """FIX Group - NoDistribInsts"""

    DistribPaymentMethod: Optional[int] = Field(None, alias='477', description='')
    DistribPercentage: Optional[float] = Field(None, alias='512', description='')
    CashDistribCurr: Optional[str] = Field(None, alias='478', description='')
    CashDistribAgentName: Optional[str] = Field(None, alias='498', description='')
    CashDistribAgentCode: Optional[str] = Field(None, alias='499', description='')
    CashDistribAgentAcctNumber: Optional[str] = Field(None, alias='500', description='')
    CashDistribPayRef: Optional[str] = Field(None, alias='501', description='')
    CashDistribAgentAcctName: Optional[str] = Field(None, alias='502', description='')



class RgstDistInstGrpComponent(FIXComponentBase):
    """FIX Component - RgstDistInstGrp"""


