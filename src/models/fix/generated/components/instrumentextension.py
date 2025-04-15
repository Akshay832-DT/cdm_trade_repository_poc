"""
FIX Component Model - InstrumentExtension
"""

from ..base import FIXComponentBase
from .attrbgrp import AttrbGrpComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List




class InstrumentExtensionComponent(FIXComponentBase):
    """FIX Component - InstrumentExtension"""
    DeliveryForm: Optional[int] = Field(None, alias='668', description='')
    PctAtRisk: Optional[float] = Field(None, alias='869', description='')
    AttrbGrp: Optional[AttrbGrpComponent] = Field(None, description='')

