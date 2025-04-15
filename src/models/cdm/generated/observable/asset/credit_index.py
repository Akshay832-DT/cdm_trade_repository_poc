from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
    from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
    from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.field_with_meta_index_annex_source_enum import FieldWithMetaIndexAnnexSourceEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.product.asset.credit_seniority_enum import CreditSeniorityEnum
    from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation
    from src.models.cdm.generated.product.asset.settled_entity_matrix import SettledEntityMatrix
    from src.models.cdm.generated.product.asset.tranche import Tranche

class CreditIndex(CdmModelBase):
    """Specification of an index based on credit risk, typically composed using corporate debt instruments in a region or industry sector, e.g. the iTraxx indices."""
    identifier: List[ForwardRef("AssetIdentifier")] = Field(None, description="Asset Identifiers are used to uniquely identify an Asset, using a specified Asset Identifier Type.")
    taxonomy: List[ForwardRef("Taxonomy")] = Field(None, description="Defines the taxonomy of an object by combining a taxonomy source (i.e. the rules to classify the object) and a value (i.e. the output of those rules on the object.")
    is_exchange_listed: bool = Field(None, description="Defines whether the Asset is listed on a public exchange.")
    exchange: ForwardRef("LegalEntity") = Field(None, description="If the Asset is listed, defines the public exchange of the listing.")
    related_exchange: List[ForwardRef("LegalEntity")] = Field(None, description="Provides the related Exchanges, if applicable.")
    name: ForwardRef("FieldWithMetaString") = Field(None, description="A description of the Index.")
    provider: ForwardRef("LegalEntity") = Field(None, description="The organisation that creates or maintains the Index.")
    asset_class: ForwardRef("AssetClassEnum") = Field(None, description="The Asset Class of the Index.")
    index_series: int = Field(None, description="A CDS index series identifier, e.g. 1, 2, 3 etc.")
    index_annex_version: int = Field(None, description="A CDS index series version identifier, e.g. 1, 2, 3 etc.")
    index_annex_date: str = Field(None, description="A CDS index series annex date.")
    index_annex_source: ForwardRef("FieldWithMetaIndexAnnexSourceEnum") = Field(None, description="A CDS index series annex source.")
    excluded_reference_entity: List[ForwardRef("ReferenceInformation")] = Field(None, description="Excluded reference entity.")
    tranche: ForwardRef("Tranche") = Field(None, description="This element contains CDS tranche terms.")
    settled_entity_matrix: ForwardRef("SettledEntityMatrix") = Field(None, description="Used to specify the Relevant Settled Entity Matrix when there are settled entities at the time of the trade.")
    index_factor: float = Field(None, description="Index Factor is the index version factor or percent, expressed as an absolute decimal value between 0 and 1, that multiplied by the original notional amount yields the notional amount covered by the seller of protection.")
    seniority: ForwardRef("CreditSeniorityEnum") = Field(None, description="Seniority of debt instruments comprising the index.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.asset_class_enum import AssetClassEnum
from src.models.cdm.generated.base.staticdata.asset.common.asset_identifier import AssetIdentifier
from src.models.cdm.generated.base.staticdata.asset.common.taxonomy import Taxonomy
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.field_with_meta_index_annex_source_enum import FieldWithMetaIndexAnnexSourceEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.product.asset.credit_seniority_enum import CreditSeniorityEnum
from src.models.cdm.generated.product.asset.reference_information import ReferenceInformation
from src.models.cdm.generated.product.asset.settled_entity_matrix import SettledEntityMatrix
from src.models.cdm.generated.product.asset.tranche import Tranche
CreditIndex.model_rebuild()
