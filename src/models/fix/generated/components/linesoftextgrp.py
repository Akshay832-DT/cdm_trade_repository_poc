"""
FIX Component Model - LinesOfTextGrp
"""

from ..base import FIXComponentBase
from datetime import date, datetime, time
from pydantic import Field
from typing import Optional, List


class NoLinesOfTextGroup(FIXComponentBase):

    """FIX Group - NoLinesOfText"""

    Text: str = Field(alias='58', description='')
    EncodedTextLen: Optional[int] = Field(None, alias='354', description='')
    EncodedText: Optional[str] = Field(None, alias='355', description='')



class LinesOfTextGrpComponent(FIXComponentBase):
    """FIX Component - LinesOfTextGrp"""


