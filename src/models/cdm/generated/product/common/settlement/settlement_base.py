from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.product.common.settlement.settlement_centre_enum import SettlementCentreEnum
    from src.models.cdm.generated.product.common.settlement.settlement_date import SettlementDate
    from src.models.cdm.generated.product.common.settlement.settlement_provision import SettlementProvision
    from src.models.cdm.generated.product.common.settlement.settlement_type_enum import SettlementTypeEnum
    from src.models.cdm.generated.product.common.settlement.standard_settlement_style_enum import StandardSettlementStyleEnum
    from src.models.cdm.generated.product.common.settlement.transfer_settlement_enum import TransferSettlementEnum

class SettlementBase(CdmModelBase):
    """A base class to be extended by the SettlementTerms class."""
    settlement_type: ForwardRef("SettlementTypeEnum") = Field(description="Whether the settlement will be cash, physical, by election, ...")
    transfer_settlement_type: ForwardRef("TransferSettlementEnum") = Field(None, description="The qualification as to how the transfer will settle, e.g. a DvP settlement.")
    settlement_currency: ForwardRef("FieldWithMetaString") = Field(None, description="The settlement currency is to be specified when the Settlement Amount cannot be known in advance. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
    settlement_date: ForwardRef("SettlementDate") = Field(None, description="The date on which the settlement amount will be paid, subject to adjustment in accordance with any applicable business day convention. This component would not be present for a mandatory early termination provision where the cash settlement payment date is the mandatory early termination date.")
    settlement_centre: ForwardRef("SettlementCentreEnum") = Field(None, description="Optional settlement centre as an enumerated list: Euroclear, Clearstream.")
    settlement_provision: ForwardRef("SettlementProvision") = Field(None, description="Optionally defines the parameters that regulate a settlement.")
    standard_settlement_style: ForwardRef("StandardSettlementStyleEnum") = Field(None, description="Settlement Style.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.product.common.settlement.settlement_centre_enum import SettlementCentreEnum
from src.models.cdm.generated.product.common.settlement.settlement_date import SettlementDate
from src.models.cdm.generated.product.common.settlement.settlement_provision import SettlementProvision
from src.models.cdm.generated.product.common.settlement.settlement_type_enum import SettlementTypeEnum
from src.models.cdm.generated.product.common.settlement.standard_settlement_style_enum import StandardSettlementStyleEnum
from src.models.cdm.generated.product.common.settlement.transfer_settlement_enum import TransferSettlementEnum
SettlementBase.model_rebuild()
