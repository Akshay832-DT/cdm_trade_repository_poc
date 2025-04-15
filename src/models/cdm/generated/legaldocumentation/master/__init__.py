"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.master.equity_master_confirmation import EquityMasterConfirmation
    from src.models.cdm.generated.legaldocumentation.master.equity_swap_master_confirmation2018 import EquitySwapMasterConfirmation2018
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause import MasterAgreementClause
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_identifier_enum import MasterAgreementClauseIdentifierEnum
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_clause_variant import MasterAgreementClauseVariant
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_schedule import MasterAgreementSchedule
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_type_enum import MasterAgreementTypeEnum
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_variable_set import MasterAgreementVariableSet
    from src.models.cdm.generated.legaldocumentation.master.master_agreement_variant_identifier_enum import MasterAgreementVariantIdentifierEnum
    from src.models.cdm.generated.legaldocumentation.master.master_confirmation_annex_type_enum import MasterConfirmationAnnexTypeEnum
    from src.models.cdm.generated.legaldocumentation.master.master_confirmation_base import MasterConfirmationBase
    from src.models.cdm.generated.legaldocumentation.master.master_confirmation_type_enum import MasterConfirmationTypeEnum
    from src.models.cdm.generated.legaldocumentation.master.nationalization_or_insolvency_or_delisting_event_enum import NationalizationOrInsolvencyOrDelistingEventEnum
