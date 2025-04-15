from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.cash import Cash
    from src.models.cdm.generated.base.staticdata.asset.common.commodity import Commodity
    from src.models.cdm.generated.base.staticdata.asset.common.digital_asset import DigitalAsset
    from src.models.cdm.generated.base.staticdata.asset.common.instrument import Instrument

class Asset(CdmModelBase):
    """An Asset is defined as something that can be owned and transferred in the financial markets. As a choice data type, one and only one of the attributes must be used."""
    cash: ForwardRef("Cash") = Field(None, description="An Asset that consists solely of a monetary holding in a currency.")
    commodity: ForwardRef("Commodity") = Field(None, description="An Asset comprised of raw or refined materials or agricultural products, eg gold, oil or wheat.")
    digital_asset: ForwardRef("DigitalAsset") = Field(None, description="An Asset that exists only in digital form, eg Bitcoin or Ethereum; excludes the digital representation of other Assets.")
    instrument: ForwardRef("Instrument") = Field(None, description="An asset that is issued by one party to one or more others; Instrument is also a choice data type.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.cash import Cash
from src.models.cdm.generated.base.staticdata.asset.common.commodity import Commodity
from src.models.cdm.generated.base.staticdata.asset.common.digital_asset import DigitalAsset
from src.models.cdm.generated.base.staticdata.asset.common.instrument import Instrument
Asset.model_rebuild()
