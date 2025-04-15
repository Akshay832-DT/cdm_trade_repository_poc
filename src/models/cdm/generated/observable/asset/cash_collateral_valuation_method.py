from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.observable.asset.csa_type_enum import CsaTypeEnum
    from src.models.cdm.generated.observable.asset.party_determination_enum import PartyDeterminationEnum

class CashCollateralValuationMethod(CdmModelBase):
    """This type is a generic structure that can represent the parameters of several mid-market valuation and replacement value methods described in the 2021 ISDA Definitions."""
    applicable_csa: ForwardRef("CsaTypeEnum") = Field(None, description="This may be used to specify what type of CSA (credit support annex/agreement) is to be used for cash settlement purposes.")
    cash_collateral_currency: str = Field(None, description="This may be used to indicate the currency of cash collateral for cash settlement purposes.")
    cash_collateral_interest_rate: ForwardRef("FieldWithMetaString") = Field(None, description="This may be used to indicate the interest rate to be used for cash collateral for cash settlement purposes.")
    agreed_discount_rate: ForwardRef("FieldWithMetaString") = Field(None, description="This may be used to indicate the discount rate to be used for cash collateral for cash settlement purposes.")
    protected_party: List[ForwardRef("PartyDeterminationEnum")] = Field(None, description="This may be used to specify which party is protected (e.g. under Replacement Value cash settlement methods).")
    prescribed_documentation_adjustment: bool = Field(None, description="This may be used to indicate that 'prescribed documentation adjustment' is applicable.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.observable.asset.csa_type_enum import CsaTypeEnum
from src.models.cdm.generated.observable.asset.party_determination_enum import PartyDeterminationEnum
CashCollateralValuationMethod.model_rebuild()
