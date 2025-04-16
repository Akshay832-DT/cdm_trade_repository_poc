"""CDM Product model."""
from typing import Optional
from pydantic import Field
from src.models.cdm.generated.base.base import CdmModelBase
from src.models.cdm.generated.product.contract_terms import ContractTerms

class Product(CdmModelBase):
    """
    A class to specify a financial product through its economic terms, identification, and taxonomy.
    """
    contract_terms: Optional[ContractTerms] = Field(None, description="The economic terms that define and govern the financial product.") 