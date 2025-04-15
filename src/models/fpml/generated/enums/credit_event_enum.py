"""
FpML Enumeration Type - CreditEventEnum
"""

from enum import Enum

class CreditEventEnum(str, Enum):
    Bankruptcy = "Bankruptcy"
    FailureToPay = "FailureToPay"
    Restructuring = "Restructuring"
    ObligationDefault = "ObligationDefault"
    ObligationAcceleration = "ObligationAcceleration"
