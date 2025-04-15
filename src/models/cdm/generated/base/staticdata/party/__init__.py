"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.party.account import Account
    from src.models.cdm.generated.base.staticdata.party.account_type_enum import AccountTypeEnum
    from src.models.cdm.generated.base.staticdata.party.address import Address
    from src.models.cdm.generated.base.staticdata.party.ancillary_entity import AncillaryEntity
    from src.models.cdm.generated.base.staticdata.party.ancillary_party import AncillaryParty
    from src.models.cdm.generated.base.staticdata.party.ancillary_role_enum import AncillaryRoleEnum
    from src.models.cdm.generated.base.staticdata.party.business_unit import BusinessUnit
    from src.models.cdm.generated.base.staticdata.party.buyer_seller import BuyerSeller
    from src.models.cdm.generated.base.staticdata.party.contact_information import ContactInformation
    from src.models.cdm.generated.base.staticdata.party.counterparty import Counterparty
    from src.models.cdm.generated.base.staticdata.party.counterparty_role_enum import CounterpartyRoleEnum
    from src.models.cdm.generated.base.staticdata.party.entity_type_enum import EntityTypeEnum
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.base.staticdata.party.natural_person import NaturalPerson
    from src.models.cdm.generated.base.staticdata.party.natural_person_role import NaturalPersonRole
    from src.models.cdm.generated.base.staticdata.party.natural_person_role_enum import NaturalPersonRoleEnum
    from src.models.cdm.generated.base.staticdata.party.party import Party
    from src.models.cdm.generated.base.staticdata.party.party_contact_information import PartyContactInformation
    from src.models.cdm.generated.base.staticdata.party.party_identifier import PartyIdentifier
    from src.models.cdm.generated.base.staticdata.party.party_identifier_type_enum import PartyIdentifierTypeEnum
    from src.models.cdm.generated.base.staticdata.party.party_reference_payer_receiver import PartyReferencePayerReceiver
    from src.models.cdm.generated.base.staticdata.party.party_role import PartyRole
    from src.models.cdm.generated.base.staticdata.party.party_role_enum import PartyRoleEnum
    from src.models.cdm.generated.base.staticdata.party.payer_receiver import PayerReceiver
    from src.models.cdm.generated.base.staticdata.party.payer_receiver_enum import PayerReceiverEnum
    from src.models.cdm.generated.base.staticdata.party.person_identifier import PersonIdentifier
    from src.models.cdm.generated.base.staticdata.party.person_identifier_type_enum import PersonIdentifierTypeEnum
    from src.models.cdm.generated.base.staticdata.party.reference_bank import ReferenceBank
    from src.models.cdm.generated.base.staticdata.party.reference_banks import ReferenceBanks
    from src.models.cdm.generated.base.staticdata.party.related_party import RelatedParty
    from src.models.cdm.generated.base.staticdata.party.telephone_number import TelephoneNumber
    from src.models.cdm.generated.base.staticdata.party.telephone_type_enum import TelephoneTypeEnum
