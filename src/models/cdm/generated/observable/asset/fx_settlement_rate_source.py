from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.fx_information_source import FxInformationSource

class FxSettlementRateSource(CdmModelBase):
    """The source of the Foreign Exchange settlement rate."""
    settlement_rate_option: ForwardRef("FieldWithMetaString") = Field(None, description="Indicates that an officially defined rate settlement rate option will be the used for the fixing.")
    nonstandard_settlement_rate: ForwardRef("FxInformationSource") = Field(None, description="Indicates that a non-standard rate source will be used for the fixing.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.fx_information_source import FxInformationSource
FxSettlementRateSource.model_rebuild()
