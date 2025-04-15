from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class MasterConfirmationAnnexTypeEnum(CdmModelBase):
    """The enumerated values to specify the type of annex to be used with master confirmation agreement governing the transaction."""
    # Enum values
    ISDA2004IndexVarianceSwapAmericasInterdealer: ClassVar[str] = "ISDA2004IndexVarianceSwapAmericasInterdealer"
    ISDA2004ShareVarianceSwapAmericasInterdealer: ClassVar[str] = "ISDA2004ShareVarianceSwapAmericasInterdealer"
    ISDA2007DispersionVarianceSwapEuropean: ClassVar[str] = "ISDA2007DispersionVarianceSwapEuropean"
    ISDA2007EquityFinanceSwapEuropean: ClassVar[str] = "ISDA2007EquityFinanceSwapEuropean"
    ISDA2007IndexVarianceSwapAmericasInterdealer: ClassVar[str] = "ISDA2007IndexVarianceSwapAmericasInterdealer"
    ISDA2007ShareVarianceSwapAmericasInterdealer: ClassVar[str] = "ISDA2007ShareVarianceSwapAmericasInterdealer"
    ISDA2007VarianceOptionEuropean: ClassVar[str] = "ISDA2007VarianceOptionEuropean"
    ISDA2008EquityFinanceSwapAsiaExcludingJapan: ClassVar[str] = "ISDA2008EquityFinanceSwapAsiaExcludingJapan"
    ISDA2008EquityFinanceSwapAsiaExcludingJapanRev1: ClassVar[str] = "ISDA2008EquityFinanceSwapAsiaExcludingJapanRev1"
    ISDA2008EquityOptionAsiaExcludingJapan: ClassVar[str] = "ISDA2008EquityOptionAsiaExcludingJapan"
    ISDA2008EquityOptionAsiaExcludingJapanRev1: ClassVar[str] = "ISDA2008EquityOptionAsiaExcludingJapanRev1"
    ISDA2008EquityOptionJapan: ClassVar[str] = "ISDA2008EquityOptionJapan"
    ISDA2009ClosedMarketsOptionsAsiaExcludingJapan: ClassVar[str] = "ISDA2009ClosedMarketsOptionsAsiaExcludingJapan"
    ISDA2009EquityEuropeanIS: ClassVar[str] = "ISDA2009EquityEuropeanIS"
    ISDA2009EquityEuropeanInterdealerSS: ClassVar[str] = "ISDA2009EquityEuropeanInterdealerSS"
    ISDA2009IndexShareOptionAmericas: ClassVar[str] = "ISDA2009IndexShareOptionAmericas"
    ISDA2009IndexSwapEuropeanInterdealer: ClassVar[str] = "ISDA2009IndexSwapEuropeanInterdealer"
    ISDA2009IndexSwapPanAsiaInterdealer: ClassVar[str] = "ISDA2009IndexSwapPanAsiaInterdealer"
    ISDA2009ShareSwapPanAsia: ClassVar[str] = "ISDA2009ShareSwapPanAsia"
    ISDA2010FairValueShareSwapEuropeanInterdealer: ClassVar[str] = "ISDA2010FairValueShareSwapEuropeanInterdealer"
    ISDA2010IndexShareOptionEMEAInterdealer: ClassVar[str] = "ISDA2010IndexShareOptionEMEAInterdealer"


# Import after class definition to avoid circular imports
MasterConfirmationAnnexTypeEnum.model_rebuild()
