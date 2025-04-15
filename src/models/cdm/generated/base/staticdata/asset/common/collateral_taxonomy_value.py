from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.eu_emir__eligible_collateral_enum import EU_EMIR_EligibleCollateralEnum
    from src.models.cdm.generated.base.staticdata.asset.common.uk_emir__eligible_collateral_enum import UK_EMIR_EligibleCollateralEnum
    from src.models.cdm.generated.base.staticdata.asset.common.us_cftc_pr__eligible_collateral_enum import US_CFTC_PR_EligibleCollateralEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class CollateralTaxonomyValue(CdmModelBase):
    """Specifies the collateral taxonomy value, either as a specified enumeration or as a string."""
    eu_emir__eligible_collateral: List[ForwardRef("EU_EMIR_EligibleCollateralEnum")] = Field(None, description="Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM")
    uk_emir__eligible_collateral: List[ForwardRef("UK_EMIR_EligibleCollateralEnum")] = Field(None, description="Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.")
    us_cftc_pr__eligible_collateral: List[ForwardRef("US_CFTC_PR_EligibleCollateralEnum")] = Field(None, description="Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators’ margin rules, the precise definitions or application of those rules could differ between the two rules.")
    non_enumerated_taxonomy_value: List[ForwardRef("FieldWithMetaString")] = Field(None, description="Identifies the taxonomy value when not specified as an enumeration.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.eu_emir__eligible_collateral_enum import EU_EMIR_EligibleCollateralEnum
from src.models.cdm.generated.base.staticdata.asset.common.uk_emir__eligible_collateral_enum import UK_EMIR_EligibleCollateralEnum
from src.models.cdm.generated.base.staticdata.asset.common.us_cftc_pr__eligible_collateral_enum import US_CFTC_PR_EligibleCollateralEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
CollateralTaxonomyValue.model_rebuild()
