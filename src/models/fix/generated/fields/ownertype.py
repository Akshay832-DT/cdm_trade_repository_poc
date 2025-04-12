
from .base import FIXFieldBase
from .types import FIXInt

class OwnerType(FIXFieldBase):
    """FIX OwnerType field."""
    tag: str = "522"
    name: str = "OwnerType"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 1: INDIVIDUAL_INVESTOR
    # 2: PUBLIC_COMPANY
    # 3: PRIVATE_COMPANY
    # 4: INDIVIDUAL_TRUSTEE
    # 5: COMPANY_TRUSTEE
    # 6: PENSION_PLAN
    # 7: CUSTODIAN_UNDER_GIFTS_TO_MINORS_ACT
    # 8: TRUSTS
    # 9: FIDUCIARIES
    # 10: NETWORKING_SUB_ACCOUNT
    # 11: NON_PROFIT_ORGANIZATION
    # 12: CORPORATE_BODY
    # 13: NOMINEE
