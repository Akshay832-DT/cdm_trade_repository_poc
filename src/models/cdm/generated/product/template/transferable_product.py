from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar
from src.models.cdm.generated.product.template.economic_terms import EconomicTerms

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.cash import Cash
    from src.models.cdm.generated.base.staticdata.asset.common.commodity import Commodity
    from src.models.cdm.generated.base.staticdata.asset.common.digital_asset import DigitalAsset
    from src.models.cdm.generated.base.staticdata.asset.common.instrument import Instrument

class TransferableProduct(CdmModelBase):
    """A TransferableProduct is a type of financial product which can be held or transferred, represented as an Asset with the addition of specific EconomicTerms."""
    cash: Optional[Dict[str, Any]] = Field(None, description="An Asset that consists solely of a monetary holding in a currency.")
    commodity: Optional[Dict[str, Any]] = Field(None, description="An Asset comprised of raw or refined materials or agricultural products, eg gold, oil or wheat.")
    digital_asset: Optional[Dict[str, Any]] = Field(None, alias="digitalAsset", description="An Asset that exists only in digital form, eg Bitcoin or Ethereum; excludes the digital representation of other Assets.")
    instrument: Optional[Dict[str, Any]] = Field(None, description="An asset that is issued by one party to one or more others; Instrument is also a choice data type.")
    economic_terms: Union[Dict[str, Any], EconomicTerms] = Field(..., alias="economicTerms", description="The price forming features, including payouts and provisions.")

    @model_validator(mode='after')
    def validate_types(self) -> 'TransferableProduct':
        """Validate that the types of the attributes are correct."""
        try:
            if self.cash is not None and isinstance(self.cash, dict):
                self.cash = Cash(**self.cash)
            if self.commodity is not None and isinstance(self.commodity, dict):
                self.commodity = Commodity(**self.commodity)
            if self.digital_asset is not None and isinstance(self.digital_asset, dict):
                self.digital_asset = DigitalAsset(**self.digital_asset)
            if self.instrument is not None and isinstance(self.instrument, dict):
                self.instrument = Instrument(**self.instrument)
            
            if isinstance(self.economic_terms, dict):
                # Ensure payout is at least an empty list if not present
                if 'payout' not in self.economic_terms:
                    self.economic_terms['payout'] = []
                self.economic_terms = EconomicTerms(**self.economic_terms)
            elif not isinstance(self.economic_terms, EconomicTerms):
                raise ValueError("economic_terms must be a valid EconomicTerms object or dictionary")
        except Exception as e:
            raise ValueError(f"Failed to validate TransferableProduct: {str(e)}")
        return self

TransferableProduct.model_rebuild()
