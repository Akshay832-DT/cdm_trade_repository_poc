"""
FIX 4.4 Field Types

This module contains enums for FIX field types.
"""
from enum import Enum
from datetime import datetime, date, time
from typing import List, Optional, Union, Dict

class FIXFieldType(Enum):
    """Enum representing FIX field types."""
    AMT = 'AMT'
    BOOLEAN = 'BOOLEAN'
    CHAR = 'CHAR'
    COUNTRY = 'COUNTRY'
    CURRENCY = 'CURRENCY'
    DATA = 'DATA'
    EXCHANGE = 'EXCHANGE'
    FLOAT = 'FLOAT'
    INT = 'INT'
    LENGTH = 'LENGTH'
    LOCALMKTDATE = 'LOCALMKTDATE'
    MONTHYEAR = 'MONTHYEAR'
    MULTIPLEVALUESTRING = 'MULTIPLEVALUESTRING'
    NUMINGROUP = 'NUMINGROUP'
    PERCENTAGE = 'PERCENTAGE'
    PRICE = 'PRICE'
    PRICEOFFSET = 'PRICEOFFSET'
    QTY = 'QTY'
    SEQNUM = 'SEQNUM'
    STRING = 'STRING'
    UTCDATEONLY = 'UTCDATEONLY'
    UTCTIMEONLY = 'UTCTIMEONLY'
    UTCTIMESTAMP = 'UTCTIMESTAMP'
