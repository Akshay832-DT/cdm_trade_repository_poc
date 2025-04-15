"""
FIX Component Model - InstrmtStrkPxGrp
"""

from ..base import FIXComponentBase
from .instrument import InstrumentComponent
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoStrikesGroup(FIXComponentBase):

    """FIX Group - NoStrikes"""

    Instrument: InstrumentComponent



class InstrmtStrkPxGrpComponent(FIXComponentBase):
    """FIX Component - InstrmtStrkPxGrp"""


