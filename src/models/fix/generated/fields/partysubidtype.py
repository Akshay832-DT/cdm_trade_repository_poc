
from .base import FIXFieldBase
from .types import FIXInt

class PartySubIDType(FIXFieldBase):
    """FIX PartySubIDType field."""
    tag: str = "803"
    name: str = "PartySubIDType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: FIRM
    # 2: PERSON
    # 3: SYSTEM
    # 4: APPLICATION
    # 5: FULL_LEGAL_NAME_OF_FIRM
    # 6: POSTAL_ADDRESS
    # 7: PHONE_NUMBER
    # 8: EMAIL_ADDRESS
    # 9: CONTACT_NAME
    # 10: SECURITIES_ACCOUNT_NUMBER
    # 11: REGISTRATION_NUMBER
    # 12: REGISTERED_ADDRESS_FOR_CONFIRMATION
    # 13: REGULATORY_STATUS
    # 14: REGISTRATION_NAME
    # 15: CASH_ACCOUNT_NUMBER
    # 16: BIC
    # 17: CSD_PARTICIPANT_MEMBER_CODE
    # 18: REGISTERED_ADDRESS
    # 19: FUND_ACCOUNT_NAME
    # 20: TELEX_NUMBER
    # 21: FAX_NUMBER
    # 22: SECURITIES_ACCOUNT_NAME
    # 23: CASH_ACCOUNT_NAME
    # 24: DEPARTMENT
    # 25: LOCATION_DESK
    # 26: POSITION_ACCOUNT_TYPE
