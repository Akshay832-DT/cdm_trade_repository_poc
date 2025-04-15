from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class DividendDateReferenceEnum(CdmModelBase):
    """The enumerated values to specify the date by reference to which the dividend will be paid."""
    # Enum values
    AdHocDate: ClassVar[str] = "AdHocDate"
    CashSettlePaymentDateExDiv: ClassVar[str] = "CashSettlePaymentDateExDiv"
    CashSettlePaymentDateIssuerPayment: ClassVar[str] = "CashSettlePaymentDateIssuerPayment"
    CashSettlementPaymentDate: ClassVar[str] = "CashSettlementPaymentDate"
    CumulativeEquityExDiv: ClassVar[str] = "CumulativeEquityExDiv"
    CumulativeEquityExDivBeforeReset: ClassVar[str] = "CumulativeEquityExDivBeforeReset"
    CumulativeEquityPaid: ClassVar[str] = "CumulativeEquityPaid"
    CumulativeEquityPaidBeforeReset: ClassVar[str] = "CumulativeEquityPaidBeforeReset"
    CumulativeEquityPaidInclReset: ClassVar[str] = "CumulativeEquityPaidInclReset"
    CumulativeInterestExDiv: ClassVar[str] = "CumulativeInterestExDiv"
    CumulativeInterestPaid: ClassVar[str] = "CumulativeInterestPaid"
    CumulativeInterestPaidBeforeReset: ClassVar[str] = "CumulativeInterestPaidBeforeReset"
    CumulativeInterestPaidInclReset: ClassVar[str] = "CumulativeInterestPaidInclReset"
    DividendPaymentDate: ClassVar[str] = "DividendPaymentDate"
    DividendValuationDate: ClassVar[str] = "DividendValuationDate"
    EquityPaymentDate: ClassVar[str] = "EquityPaymentDate"
    ExDate: ClassVar[str] = "ExDate"
    FloatingAmountPaymentDate: ClassVar[str] = "FloatingAmountPaymentDate"
    FollowingPaymentDate: ClassVar[str] = "FollowingPaymentDate"
    RecordDate: ClassVar[str] = "RecordDate"
    SharePayment: ClassVar[str] = "SharePayment"
    TerminationDate: ClassVar[str] = "TerminationDate"
    TradeDate: ClassVar[str] = "TradeDate"
    UnwindExDiv: ClassVar[str] = "UnwindExDiv"
    UnwindOrEquityExDiv: ClassVar[str] = "UnwindOrEquityExDiv"
    UnwindOrEquityPaid: ClassVar[str] = "UnwindOrEquityPaid"
    UnwindOrInterestExDiv: ClassVar[str] = "UnwindOrInterestExDiv"
    UnwindOrInterestPaid: ClassVar[str] = "UnwindOrInterestPaid"
    UnwindPaid: ClassVar[str] = "UnwindPaid"


# Import after class definition to avoid circular imports
DividendDateReferenceEnum.model_rebuild()
