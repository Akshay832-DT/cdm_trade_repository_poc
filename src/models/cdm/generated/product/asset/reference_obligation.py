from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.common.loan import Loan
    from src.models.cdm.generated.base.staticdata.asset.common.security import Security
    from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
    from src.models.cdm.generated.metafields.reference_with_meta_legal_entity import ReferenceWithMetaLegalEntity

class ReferenceObligation(CdmModelBase):
    """A class to specify the reference obligation that is associated with a credit derivative instrument."""
    security: ForwardRef("Security") = Field(None, description="Identifies the underlying asset when it is a security, such as a bond or convertible bond. The security data type requires one or more productIdentifiers, specificaiton of the security type (e.g. debt), and includes optional attributes to specify a debt class, such as asset-backed, as well as seniority.")
    loan: ForwardRef("Loan") = Field(None, description="Identifies the underlying asset when it is a loan.")
    primary_obligor: ForwardRef("LegalEntity") = Field(None, description="The entity primarily responsible for repaying debt to a creditor as a result of borrowing or issuing bonds. ISDA 2003 Term: Primary Obligor.")
    primary_obligor_reference: ForwardRef("ReferenceWithMetaLegalEntity") = Field(None, description="A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the primary obligor.")
    guarantor: ForwardRef("LegalEntity") = Field(None, description="The party that guarantees by way of a contractual arrangement to pay the debts of an obligor if the obligor is unable to make the required payments itself. ISDA 2003 Term: Guarantor.")
    guarantor_reference: str = Field(None, description="A pointer style reference to a reference entity defined elsewhere in the document. Used when the reference entity is the guarantor.")
    standard_reference_obligation: bool = Field(None, description="Indicates if the reference obligation is a Standard Reference Obligation. ISDA 2014 Term: Standard Reference Obligation.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.base.staticdata.asset.common.loan import Loan
from src.models.cdm.generated.base.staticdata.asset.common.security import Security
from src.models.cdm.generated.base.staticdata.party.legal_entity import LegalEntity
from src.models.cdm.generated.metafields.reference_with_meta_legal_entity import ReferenceWithMetaLegalEntity
ReferenceObligation.model_rebuild()
