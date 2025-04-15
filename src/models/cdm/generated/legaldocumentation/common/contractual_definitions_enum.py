from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class ContractualDefinitionsEnum(CdmModelBase):
    """The enumerated values to specify a set of standard contract definitions relevant to the transaction."""
    # Enum values
    ISDA1991InterestRate: ClassVar[str] = "ISDA1991InterestRate"
    ISDA1993CommodityDerivatives: ClassVar[str] = "ISDA1993CommodityDerivatives"
    ISDA1996EquityDerivatives: ClassVar[str] = "ISDA1996EquityDerivatives"
    ISDA1997Bullion: ClassVar[str] = "ISDA1997Bullion"
    ISDA1997GovernmentBondOption: ClassVar[str] = "ISDA1997GovernmentBondOption"
    ISDA1998FxAndCurrencyOption: ClassVar[str] = "ISDA1998FxAndCurrencyOption"
    ISDA1999CreditDerivatives: ClassVar[str] = "ISDA1999CreditDerivatives"
    ISDA2000: ClassVar[str] = "ISDA2000"
    ISDA2002EquityDerivatives: ClassVar[str] = "ISDA2002EquityDerivatives"
    ISDA2003CreditDerivatives: ClassVar[str] = "ISDA2003CreditDerivatives"
    ISDA2004Novation: ClassVar[str] = "ISDA2004Novation"
    ISDA2005Commodity: ClassVar[str] = "ISDA2005Commodity"
    ISDA2006: ClassVar[str] = "ISDA2006"
    ISDA2006InflationDerivatives: ClassVar[str] = "ISDA2006InflationDerivatives"
    ISDA2008InflationDerivatives: ClassVar[str] = "ISDA2008InflationDerivatives"
    ISDA2011EquityDerivatives: ClassVar[str] = "ISDA2011EquityDerivatives"
    ISDA2014CreditDerivatives: ClassVar[str] = "ISDA2014CreditDerivatives"
    ISDA2021InterestRateDerivatives: ClassVar[str] = "ISDA2021InterestRateDerivatives"
    ISDA2022VerifiedCarbonCredit: ClassVar[str] = "ISDA2022VerifiedCarbonCredit"
    ISDA2023DigitalAssetDerivatives: ClassVar[str] = "ISDA2023DigitalAssetDerivatives"


# Import after class definition to avoid circular imports
ContractualDefinitionsEnum.model_rebuild()
