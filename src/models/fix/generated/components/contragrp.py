"""
FIX Component Model - ContraGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoContraBrokersGroup(FIXComponentBase):

    """FIX Group - NoContraBrokers"""

    ContraBroker: Optional[str] = Field(None, alias='375', description='')
    ContraTrader: Optional[str] = Field(None, alias='337', description='')
    ContraTradeQty: Optional[float] = Field(None, alias='437', description='')
    ContraTradeTime: Optional[datetime] = Field(None, alias='438', description='')
    ContraLegRefID: Optional[str] = Field(None, alias='655', description='')



class ContraGrpComponent(FIXComponentBase):
    """FIX Component - ContraGrp"""


