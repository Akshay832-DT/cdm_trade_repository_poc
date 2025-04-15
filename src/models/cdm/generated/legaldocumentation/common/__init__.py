"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.address_for_notices import AddressForNotices
    from src.models.cdm.generated.legaldocumentation.common.agreement_name import AgreementName
    from src.models.cdm.generated.legaldocumentation.common.agreement_terms import AgreementTerms
    from src.models.cdm.generated.legaldocumentation.common.contractual_definitions_enum import ContractualDefinitionsEnum
    from src.models.cdm.generated.legaldocumentation.common.contractual_matrix import ContractualMatrix
    from src.models.cdm.generated.legaldocumentation.common.contractual_supplement_type_enum import ContractualSupplementTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.contractual_terms_supplement import ContractualTermsSupplement
    from src.models.cdm.generated.legaldocumentation.common.credit_support_document_terms_enum import CreditSupportDocumentTermsEnum
    from src.models.cdm.generated.legaldocumentation.common.credit_support_provider_terms_enum import CreditSupportProviderTermsEnum
    from src.models.cdm.generated.legaldocumentation.common.execution_location_enum import ExecutionLocationEnum
    from src.models.cdm.generated.legaldocumentation.common.governing_law_enum import GoverningLawEnum
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement import LegalAgreement
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_base import LegalAgreementBase
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_identification import LegalAgreementIdentification
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_publisher_enum import LegalAgreementPublisherEnum
    from src.models.cdm.generated.legaldocumentation.common.legal_agreement_type_enum import LegalAgreementTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.length_unit_enum import LengthUnitEnum
    from src.models.cdm.generated.legaldocumentation.common.matrix_term_enum import MatrixTermEnum
    from src.models.cdm.generated.legaldocumentation.common.matrix_type_enum import MatrixTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.other_agreement import OtherAgreement
    from src.models.cdm.generated.legaldocumentation.common.other_agreement_terms import OtherAgreementTerms
    from src.models.cdm.generated.legaldocumentation.common.resource import Resource
    from src.models.cdm.generated.legaldocumentation.common.resource_length import ResourceLength
    from src.models.cdm.generated.legaldocumentation.common.resource_type_enum import ResourceTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.specified_entity_clause_enum import SpecifiedEntityClauseEnum
    from src.models.cdm.generated.legaldocumentation.common.specified_entity_terms_enum import SpecifiedEntityTermsEnum
    from src.models.cdm.generated.legaldocumentation.common.termination_currency_condition_enum import TerminationCurrencyConditionEnum
    from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement import UmbrellaAgreement
    from src.models.cdm.generated.legaldocumentation.common.umbrella_agreement_entity import UmbrellaAgreementEntity
