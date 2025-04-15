from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class Loan(CdmModelBase):
    """Identifies a loan by referencing an asset identifier and through an optional set of attributes."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    instrument_type: ForwardRef("InstrumentTypeEnum") = Field(None, description="Identifies the type of an instrument using an enumerated list.")
    borrower: List[ForwardRef("LegalEntity")] = Field(None, description="Specifies the borrower. There can be more than one borrower. It is meant to be used in the event that there is no Bloomberg Id or the Secured List isn't applicable.")
    lien: ForwardRef("FieldWithMetaString") = Field(None, description="Specifies the seniority level of the lien.")
    facility_type: ForwardRef("FieldWithMetaString") = Field(None, description="Specifies the type of loan facility (letter of credit, revolving, ...).")
    credit_agreement_date: str = Field(None, description="Specifies the credit agreement date is the closing date (the date where the agreement has been signed) for the loans in the credit agreement. Funding of the facilities occurs on (or sometimes a little after) the Credit Agreement date. This underlier attribute is used to help identify which of the company's outstanding loans are being referenced by knowing to which credit agreement it belongs. ISDA Standards Terms Supplement term: Date of Original Credit Agreement.")
    tranche: ForwardRef("FieldWithMetaString") = Field(None, description="Denotes the loan tranche that is subject to the derivative transaction. It will typically be referenced as the Bloomberg tranche number. ISDA Standards Terms Supplement term: Bloomberg Tranche Number.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.instrument_type_enum import InstrumentTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
Loan.model_rebuild()
