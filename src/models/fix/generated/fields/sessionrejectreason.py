
from .base import FIXFieldBase
from .types import FIXInt

class SessionRejectReason(FIXFieldBase):
    """FIX SessionRejectReason field."""
    tag: str = "373"
    name: str = "SessionRejectReason"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: INVALID_TAG_NUMBER
    # 1: REQUIRED_TAG_MISSING
    # 2: TAG_NOT_DEFINED_FOR_THIS_MESSAGE_TYPE
    # 3: UNDEFINED_TAG
    # 4: TAG_SPECIFIED_WITHOUT_A_VALUE
    # 5: VALUE_IS_INCORRECT
    # 6: INCORRECT_DATA_FORMAT_FOR_VALUE
    # 7: DECRYPTION_PROBLEM
    # 8: SIGNATURE_PROBLEM
    # 9: COMP_ID_PROBLEM
    # 10: SENDING_TIME_ACCURACY_PROBLEM
    # 11: INVALID_MSG_TYPE
    # 12: XML_VALIDATION_ERROR
    # 13: TAG_APPEARS_MORE_THAN_ONCE
    # 14: TAG_SPECIFIED_OUT_OF_REQUIRED_ORDER
    # 15: REPEATING_GROUP_FIELDS_OUT_OF_ORDER
    # 16: INCORRECT_NUM_IN_GROUP_COUNT_FOR_REPEATING_GROUP
    # 17: NON
    # 99: OTHER
