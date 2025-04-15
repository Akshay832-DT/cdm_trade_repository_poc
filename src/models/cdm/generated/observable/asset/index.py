from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_interest_rate_index import FieldWithMetaInterestRateIndex
    from src.models.cdm.generated.observable.asset.credit_index import CreditIndex
    from src.models.cdm.generated.observable.asset.equity_index import EquityIndex
    from src.models.cdm.generated.observable.asset.foreign_exchange_rate_index import ForeignExchangeRateIndex
    from src.models.cdm.generated.observable.asset.other_index import OtherIndex

class Index(CdmModelBase):
    """An Index is an Observable which is computed based on the prices, rates or valuations of a number of assets that are tracked in a standardized way.  Examples include equity market indices as well as indices on interest rates, inflation and credit instruments."""
    credit_index: ForwardRef("CreditIndex") = Field(None, description="An index based on credit risk, typically composed using corporate debt instruments in a region or industry sector, e.g. the iTraxx indices.")
    equity_index: ForwardRef("EquityIndex") = Field(None, description="An index based on equity securities, e.g. the S&P 500.")
    interest_rate_index: ForwardRef("FieldWithMetaInterestRateIndex") = Field(None, description="An index based in interest rates or inflation rates in a certain market.")
    foreign_exchange_rate_index: ForwardRef("ForeignExchangeRateIndex") = Field(None, description="A rate based on the exchange of a pair of cash assets in specific currencies, e.g. USD versus GBP.")
    other_index: ForwardRef("OtherIndex") = Field(None, description="An index created by a market participant which doesn't align with the other index types.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_interest_rate_index import FieldWithMetaInterestRateIndex
from src.models.cdm.generated.observable.asset.credit_index import CreditIndex
from src.models.cdm.generated.observable.asset.equity_index import EquityIndex
from src.models.cdm.generated.observable.asset.foreign_exchange_rate_index import ForeignExchangeRateIndex
from src.models.cdm.generated.observable.asset.other_index import OtherIndex
Index.model_rebuild()
