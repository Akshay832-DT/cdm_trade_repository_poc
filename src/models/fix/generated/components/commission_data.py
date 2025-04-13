"""FIX 4.4 CommissionData component."""
from typing import Optional
from pydantic import Field
from src.models.fix.base import FIXComponentBase

class CommissionData(FIXComponentBase):
    """FIX 4.4 CommissionData component."""
    
    Commission: Optional[float] = Field(None, description='Commission amount', alias='12')
    CommissionType: Optional[int] = Field(None, description='Commission type', alias='13')
    CommissionBasis: Optional[str] = Field(None, description='Commission basis', alias='479') 