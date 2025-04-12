
from .base import FIXFieldBase
from .types import FIXChar

class PartyIDSource(FIXFieldBase):
    """FIX PartyIDSource field."""
    tag: str = "447"
    name: str = "PartyIDSource"
    type: str = "CHAR"
    value: FIXChar

    # Enum values
    # B: BIC
    # C: GENERAL_IDENTIFIER
    # D: PROPRIETARY
    # E: ISO_COUNTRY_CODE
    # F: SETTLEMENT_ENTITY_LOCATION
    # G: MIC
    # H: CSD_PARTICIPANT
    # 1: KOREAN_INVESTOR_ID
    # 2: TAIWANESE_FOREIGN_INVESTOR_ID
    # 3: TAIWANESE_TRADING_ACCT
    # 4: MALAYSIAN_CENTRAL_DEPOSITORY
    # 5: CHINESE_INVESTOR_ID
    # 6: UK_NATIONAL_INSURANCE_OR_PENSION_NUMBER
    # 7: US_SOCIAL_SECURITY_NUMBER
    # 8: US_EMPLOYER_OR_TAX_ID_NUMBER
    # 9: AUSTRALIAN_BUSINESS_NUMBER
    # A: AUSTRALIAN_TAX_FILE_NUMBER
    # I: ISITC_ACRONYM
