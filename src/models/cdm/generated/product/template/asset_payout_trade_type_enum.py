from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

class AssetPayoutTradeTypeEnum(CdmModelBase):
    """An enumerator to differentiate the different trade types used in securities finance and modelled on an AssetPayout."""
    # Enum values
    Buy_Sell_Back: ClassVar[str] = "Buy/Sell-Back"
    Repo: ClassVar[str] = "Repo"


# Import after class definition to avoid circular imports
AssetPayoutTradeTypeEnum.model_rebuild()
