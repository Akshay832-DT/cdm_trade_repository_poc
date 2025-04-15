from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.issuer_type_enum import IssuerTypeEnum
    from src.models.cdm.generated.base.staticdata.asset.common.quasi_government_issuer_type import QuasiGovernmentIssuerType
    from src.models.cdm.generated.base.staticdata.asset.common.regional_government_issuer_type import RegionalGovernmentIssuerType
    from src.models.cdm.generated.base.staticdata.asset.common.special_purpose_vehicle_issuer_type import SpecialPurposeVehicleIssuerType
    from src.models.cdm.generated.base.staticdata.asset.common.supra_national_issuer_type_enum import SupraNationalIssuerTypeEnum

class CollateralIssuerType(CdmModelBase):
    """Represents a class to allow specification of the type of entity issuing the collateral."""
    issuer_type: ForwardRef("IssuerTypeEnum") = Field(description="Specifies the origin of entity issuing the collateral.")
    supra_national_type: ForwardRef("SupraNationalIssuerTypeEnum") = Field(None, description="Specifies debt issued by international organisations and multilateral banks.")
    quasi_government_type: ForwardRef("QuasiGovernmentIssuerType") = Field(None, description="Specifies debt issues by institutions or bodies, typically constituted by statute, with a function mandated by the government and subject to government supervision inclusive of profit- and non-profit making bodies. Includes the US Agencies and GSEs and the EU concept of public sector entities. Excluding any entities which are also Regional Government.")
    regional_government_type: ForwardRef("RegionalGovernmentIssuerType") = Field(None, description="Specifies Regional government, local authority or municipal.")
    special_purpose_vehicle_type: ForwardRef("SpecialPurposeVehicleIssuerType") = Field(None, description="Specifies a subsidiary company that is formed to undertake a specific business purpose of acquisition and financing of specific assets on a potentially limited recourse basis dependent of how it is designed. E.g. asset backed securities, including securitisations.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.issuer_type_enum import IssuerTypeEnum
from src.models.cdm.generated.base.staticdata.asset.common.quasi_government_issuer_type import QuasiGovernmentIssuerType
from src.models.cdm.generated.base.staticdata.asset.common.regional_government_issuer_type import RegionalGovernmentIssuerType
from src.models.cdm.generated.base.staticdata.asset.common.special_purpose_vehicle_issuer_type import SpecialPurposeVehicleIssuerType
from src.models.cdm.generated.base.staticdata.asset.common.supra_national_issuer_type_enum import SupraNationalIssuerTypeEnum
CollateralIssuerType.model_rebuild()
