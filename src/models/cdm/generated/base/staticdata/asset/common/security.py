from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.debt_type import DebtType
    from src.models.cdm.generated.base.staticdata.asset.common.equity_type_enum import EquityTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.fund_product_type_enum import FundProductTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity

class Security(CdmModelBase):
    """Identifies a security by referencing an identifier and by specifying the sector."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    instrument_type: ForwardRef("InstrumentTypeEnum") = Field(None, description="Identifies the type of an instrument using an enumerated list.")
    debt_type: ForwardRef("DebtType") = Field(None, description="Identifies the type of debt and selected debt economics.")
    equity_type: ForwardRef("EquityTypeEnum") = Field(None, description="Identifies the type of equity.")
    fund_type: ForwardRef("FundProductTypeEnum") = Field(None, description="Identifies the type of fund.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.debt_type import DebtType
from src.models.cdm.generated.base.staticdata.asset.common.equity_type_enum import EquityTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.fund_product_type_enum import FundProductTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
Security.model_rebuild()
