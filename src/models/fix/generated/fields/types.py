"""
Type definitions for FIX fields.
"""
from typing import List, Optional, Union, Literal
from datetime import datetime, date, time
from decimal import Decimal

# Common FIX field type aliases
FIXString = str
FIXChar = str
FIXPrice = float
FIXInt = int
FIXAmt = float
FIXQty = float
FIXCurrency = str
FIXMultipleValueString = List[str]
FIXMultipleStringValue = List[str]
FIXMultipleCharValue = List[str]
FIXBoolean = bool
FIXLocalMktDate = date
FIXMonthYear = str
FIXUTCTimestamp = datetime
FIXUTCTimeOnly = time
FIXUTCDateOnly = date
FIXNumInGroup = int
FIXPercentage = float
FIXSeqNum = int
FIXLength = int
FIXData = str
FIXCountry = str
FIXExchange = str
FIXLanguage = str
FIXXMLData = str
FIXDayOfMonth = int
