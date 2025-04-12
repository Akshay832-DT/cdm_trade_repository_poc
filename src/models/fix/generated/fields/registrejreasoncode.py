
from .base import FIXFieldBase
from .types import FIXInt

class RegistRejReasonCode(FIXFieldBase):
    """FIX RegistRejReasonCode field."""
    tag: str = "507"
    name: str = "RegistRejReasonCode"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: INVALID_ACCOUNT_TYPE
    # 2: INVALID_TAX_EXEMPT_TYPE
    # 3: INVALID_OWNERSHIP_TYPE
    # 4: NO_REG_DETAILS
    # 5: INVALID_REG_SEQ_NO
    # 6: INVALID_REG_DETAILS
    # 7: INVALID_MAILING_DETAILS
    # 8: INVALID_MAILING_INSTRUCTIONS
    # 9: INVALID_INVESTOR_ID
    # 10: INVALID_INVESTOR_ID_SOURCE
    # 11: INVALID_DATE_OF_BIRTH
    # 12: INVALID_COUNTRY
    # 13: INVALID_DISTRIB_INSTNS
    # 14: INVALID_PERCENTAGE
    # 15: INVALID_PAYMENT_METHOD
    # 16: INVALID_ACCOUNT_NAME
    # 17: INVALID_AGENT_CODE
    # 18: INVALID_ACCOUNT_NUM
    # 99: OTHER
