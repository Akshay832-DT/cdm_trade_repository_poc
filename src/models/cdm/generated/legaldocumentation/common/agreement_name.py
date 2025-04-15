from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.contractual_matrix import ContractualMatrix
    from src.models.cdm.generated.legaldocumentation.common.contractual_terms_supplement import ContractualTermsSupplement
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_type_enum import LegalAgreementTypeEnum
    from src.models.cdm.generated.legaldocumentation.contract.broker_confirmation_type_enum import BrokerConfirmationTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_contractual_definitions_enum import FieldWithMetaContractualDefinitionsEnum
    from src.models.cdm.generated.metafields.field_with_meta_credit_support_agreement_type_enum import FieldWithMetaCreditSupportAgreementTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_master_agreement_type_enum import FieldWithMetaMasterAgreementTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_master_confirmation_annex_type_enum import FieldWithMetaMasterConfirmationAnnexTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_master_confirmation_type_enum import FieldWithMetaMasterConfirmationTypeEnum
    from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum

class AgreementName(CdmModelBase):
    """Specifies the agreement name through an agreement type and optional detailed sub agreement type."""
    agreement_type: ForwardRef("LegalAgreementTypeEnum") = Field(description="Specification of the legal agreement type.")
    credit_support_agreement_type: ForwardRef("FieldWithMetaCreditSupportAgreementTypeEnum") = Field(None, description="Specification of the credit support agreement type.")
    credit_support_agreement_margin_type: ForwardRef("CollateralMarginTypeEnum") = Field(None, description="specifies the type of margin for which a legal agreement is named.")
    contractual_definitions_type: List[ForwardRef("FieldWithMetaContractualDefinitionsEnum")] = Field(None, description="The definitions such as those published by ISDA that will define the terms of the trade.")
    contractual_terms_supplement: List[ForwardRef("ContractualTermsSupplement")] = Field(None, description="A contractual supplement (such as those published by ISDA) that will apply to the trade.")
    contractual_matrix: List[ForwardRef("ContractualMatrix")] = Field(None, description="A reference to a contractual matrix of elected terms/values (such as those published by ISDA) that shall be deemed to apply to the trade. The applicable matrix is identified by reference to a name and optionally a publication date. Depending on the structure of the matrix, an additional term (specified in the matrixTerm element) may be required to further identify a subset of applicable terms/values within the matrix.")
    master_agreement_type: ForwardRef("FieldWithMetaMasterAgreementTypeEnum") = Field(None, description="Specification of the master agreement type.")
    master_confirmation_type: ForwardRef("FieldWithMetaMasterConfirmationTypeEnum") = Field(None, description="The type of master confirmation executed between the parties.")
    master_confirmation_annex_type: ForwardRef("FieldWithMetaMasterConfirmationAnnexTypeEnum") = Field(None, description="The type of master confirmation annex executed between the parties.")
    other_agreement: str = Field(None, description="Definition of an agreement that is not enumerated in the CDM.")
    broker_confirmation_type: ForwardRef("BrokerConfirmationTypeEnum") = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.contractual_matrix import ContractualMatrix
from src.models.cdm.generated.legaldocumentation.common.contractual_terms_supplement import ContractualTermsSupplement
from src.models.cdm.generated.legaldocumentation.common.legal_agreement_type_enum import LegalAgreementTypeEnum
from src.models.cdm.generated.legaldocumentation.contract.broker_confirmation_type_enum import BrokerConfirmationTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_contractual_definitions_enum import FieldWithMetaContractualDefinitionsEnum
from src.models.cdm.generated.metafields.field_with_meta_credit_support_agreement_type_enum import FieldWithMetaCreditSupportAgreementTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_master_agreement_type_enum import FieldWithMetaMasterAgreementTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_master_confirmation_annex_type_enum import FieldWithMetaMasterConfirmationAnnexTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_master_confirmation_type_enum import FieldWithMetaMasterConfirmationTypeEnum
from src.models.cdm.generated.product.collateral.collateral_margin_type_enum import CollateralMarginTypeEnum
AgreementName.model_rebuild()
