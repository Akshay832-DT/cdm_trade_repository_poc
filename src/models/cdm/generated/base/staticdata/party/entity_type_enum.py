from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class EntityTypeEnum(CdmModelBase):
    """The enumerated values to specify the reference entity types corresponding to a list of types defined in the ISDA First to Default documentation."""
    # Enum values
    Asian: ClassVar[str] = "Asian"
    AustralianAndNewZealand: ClassVar[str] = "AustralianAndNewZealand"
    EuropeanEmergingMarkets: ClassVar[str] = "EuropeanEmergingMarkets"
    Japanese: ClassVar[str] = "Japanese"
    NorthAmericanHighYield: ClassVar[str] = "NorthAmericanHighYield"
    NorthAmericanInsurance: ClassVar[str] = "NorthAmericanInsurance"
    NorthAmericanInvestmentGrade: ClassVar[str] = "NorthAmericanInvestmentGrade"
    Singaporean: ClassVar[str] = "Singaporean"
    WesternEuropean: ClassVar[str] = "WesternEuropean"
    WesternEuropeanInsurance: ClassVar[str] = "WesternEuropeanInsurance"


# Import after class definition to avoid circular imports
EntityTypeEnum.model_rebuild()
