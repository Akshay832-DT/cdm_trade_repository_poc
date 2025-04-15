from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_type_enum import AssetTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.debt_type import DebtType
    from src.models.cdm.generated.base.staticdata.asset.common.equity_type_enum import EquityTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.fund_product_type_enum import FundProductTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum

class AssetType(CdmModelBase):
    """Represents a class to allow specification of the asset product type."""
    asset_type: ForwardRef("AssetTypeEnum") = Field(description="Represents a filter based on the type of collateral asset.")
    security_type: ForwardRef("InstrumentTypeEnum") = Field(None, description="Represents a filter based on the type of security.")
    debt_type: ForwardRef("DebtType") = Field(None, description="Represents a filter based on the type of bond.")
    equity_type: ForwardRef("EquityTypeEnum") = Field(None, description="Represents a filter based on the type of equity.")
    fund_type: ForwardRef("FundProductTypeEnum") = Field(None, description="Represents a filter based on the type of fund.")
    other_asset_type: List[List] = Field(None, description="Specifies the eligible asset type when not enumerated.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_type_enum import AssetTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.debt_type import DebtType
from src.models.cdm.generated.base.staticdata.asset.common.equity_type_enum import EquityTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.fund_product_type_enum import FundProductTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum
AssetType.model_rebuild()
