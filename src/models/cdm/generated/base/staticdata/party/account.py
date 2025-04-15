from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_account_type_enum import FieldWithMetaAccountTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
    from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty

class Account(CdmModelBase):
    """A class to specify an account as an account number alongside, optionally. an account name, an account type, an account beneficiary and a servicing party."""
    party_reference: ForwardRef("ReferenceWithMetaParty") = Field(None, description="A reference to the party to which the account refers to.")
    account_number: ForwardRef("FieldWithMetaString") = Field(description="The account number.")
    account_name: ForwardRef("FieldWithMetaString") = Field(None, description="The name by which the account is known.")
    account_type: ForwardRef("FieldWithMetaAccountTypeEnum") = Field(None, description="The type of account, e.g. client, house.")
    account_beneficiary: ForwardRef("ReferenceWithMetaParty") = Field(None, description="A reference to the party beneficiary of the account.")
    servicing_party: ForwardRef("ReferenceWithMetaParty") = Field(None, description="The reference to the legal entity that services the account, i.e. in the books of which the account is held.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_account_type_enum import FieldWithMetaAccountTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
from src.models.cdm.generated.metafields.reference_with_meta_party import ReferenceWithMetaParty
Account.model_rebuild()
