"""
Common field types for FIX 4.4 messages.

This module provides common field type definitions used by FIX 4.4 components and messages.
"""
from typing import Optional, Union, List, Dict, Any
from datetime import datetime, date, time
from pydantic import BaseModel, Field

# Define common type aliases
TagNum = str  # FIX tag numbers
NumInGroup = int  # Number of repeated groups
SeqNum = int  # Message sequence number
Length = int  # Length field
Boolean = str  # Y/N boolean
Price = float  # Price field
Qty = float  # Quantity field
Currency = str  # Currency code
Country = str  # Country code
Exchange = str  # Exchange identifier
UTCTimestamp = datetime  # UTC timestamp
UTCDate = date  # UTC date
UTCTimeOnly = time  # UTC time
LocalMktDate = date  # Local market date
Percentage = float  # Percentage
Amt = float  # Monetary amount
MultipleValueString = str  # Multiple value string
