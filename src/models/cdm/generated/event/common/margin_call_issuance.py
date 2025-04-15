from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.event.common.collateral_balance import CollateralBalance
    from src.models.cdm.generated.event.common.margin_call_exposure import MarginCallExposure
    from src.models.cdm.generated.event.common.margin_call_instruction_type import MarginCallInstructionType
    from src.models.cdm.generated.event.common.reg_im_role_enum import RegIMRoleEnum
    from src.models.cdm.generated.event.common.reg_margin_type_enum import RegMarginTypeEnum
    from src.models.cdm.generated.legaldocumentation.common.agreement_name import AgreementName
    from src.models.cdm.generated.metafields.reference_with_meta_collateral_portfolio import ReferenceWithMetaCollateralPortfolio
    from src.models.cdm.generated.observable.asset.money import Money
    from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria

class MarginCallIssuance(CdmModelBase):
    """Represents common attributes required for a Margin Call Issuance under a legal agreement such as a credit support document or equivalent."""
    instruction_type: ForwardRef("MarginCallInstructionType") = Field(None, description="Identifies the enumeration values to specify the call notification type, direction, specific action type.")
    party: List[ForwardRef("Party")] = Field(None, description="Represents the parties to the margin call. The cardinality is optional to address the case where both parties of the event are specified and a third party if applicable.")
    party_role: List[ForwardRef("PartyRole")] = Field(None, description="Represents the role each specified party takes in the margin call. further to the principal roles, payer and receiver.")
    clearing_broker: ForwardRef("Party") = Field(None, description="Indicates the name of the Clearing Broker FCM/DCM.")
    call_identifier: ForwardRef("Identifier") = Field(None, description="Represents a unique Identifier for a margin call message, that can be referenced throughout all points of the process.")
    call_agreement_type: ForwardRef("AgreementName") = Field(None, description="Specifies the legal agreement type the margin call is generated from and governed by.")
    agreement_minimum_transfer_amount: ForwardRef("Money") = Field(None, description="Specifies the collateral legal agreement minimum transfer amount in base currency.")
    agreement_threshold: ForwardRef("Money") = Field(None, description="Specifies the collateral legal agreement threshold amount in base currency.")
    agreement_rounding: ForwardRef("Money") = Field(None, description="Specifies the collateral legal agreement rounding in base currency.")
    reg_margin_type: ForwardRef("RegMarginTypeEnum") = Field(None, description="Identifies margin type and if related regulatory mandate")
    reg_im_role: ForwardRef("RegIMRoleEnum") = Field(None, description="Indicates the role of the party in an regulatory initial margin call instruction (i.e Pledgor party or Secured party).")
    base_currency_exposure: ForwardRef("MarginCallExposure") = Field(None, description="Represents the current mark to market value or IM calculation value of the trade portfolio as recorded by the principle (in base currency), to be referenced in a margin call.")
    collateral_portfolio: ForwardRef("ReferenceWithMetaCollateralPortfolio") = Field(None, description="Represents attributes to define the details of collateral assets within a collateral portfolio to be used in margin call messaging and contribute to collateral balances e.g securities in a collateral account recorded by the principal as held or posted.")
    independent_amount_balance: ForwardRef("CollateralBalance") = Field(None, description="Represents additional credit support amount over and above mark to market value.")
    call_amount_in_base_currency: ForwardRef("Money") = Field(description="Specifies the amount of margin being called for which accounts for margin calculation inclusive of exposure, independent amount,threshold,collateral balance, MTA, rounding increments (in base currency detailed in supporting collateral agreement).")
    recall_non_cash_collateral_description: List[ForwardRef("EligibleCollateralCriteria")] = Field(None, description="Specifies the details to describe or identify non-cash collateral eligible assets for recall purposes.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.identifier.identifier import Identifier
from src.models.cdm.generated.base.staticdata.party.party import Party
from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
from src.models.cdm.generated.event.common.collateral_balance import CollateralBalance
from src.models.cdm.generated.event.common.margin_call_exposure import MarginCallExposure
from src.models.cdm.generated.event.common.margin_call_instruction_type import MarginCallInstructionType
from src.models.cdm.generated.event.common.reg_im_role_enum import RegIMRoleEnum
from src.models.cdm.generated.event.common.reg_margin_type_enum import RegMarginTypeEnum
from src.models.cdm.generated.legaldocumentation.common.agreement_name import AgreementName
from src.models.cdm.generated.metafields.reference_with_meta_collateral_portfolio import ReferenceWithMetaCollateralPortfolio
from src.models.cdm.generated.observable.asset.money import Money
from src.models.cdm.generated.product.collateral.eligible_collateral_criteria import EligibleCollateralCriteria
MarginCallIssuance.model_rebuild()
