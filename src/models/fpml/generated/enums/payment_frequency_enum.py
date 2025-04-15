"""
FpML Enumeration Type - PaymentFrequencyEnum
"""

from enum import Enum

class PaymentFrequencyEnum(str, Enum):
    Daily = "Daily"
    Weekly = "Weekly"
    Monthly = "Monthly"
    Quarterly = "Quarterly"
    SemiAnnually = "SemiAnnually"
    Annually = "Annually"
