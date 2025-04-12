# pylint: disable=line-too-long, invalid-name, missing-function-docstring
# pylint: disable=bad-indentation, trailing-whitespace, superfluous-parens
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import
# pylint: disable=wildcard-import, wrong-import-order, missing-class-docstring
# pylint: disable=missing-module-docstring
from __future__ import annotations
from typing import List, Optional
import datetime
import inspect
from decimal import Decimal
from pydantic import Field
from rosetta.runtime.utils import (
    BaseDataClass, rosetta_condition, rosetta_resolve_attr, rosetta_resolve_deep_attr
)
from rosetta.runtime.utils import *

__all__ = ['NonTransferableProduct']


class NonTransferableProduct(BaseDataClass):
    """
    A data type to specify the financial product's economic terms, alongside the product identification and product taxonomy. The non-transferable product data type represents a product that can be traded (as part of a TradableProduct) but cannot be transferred to others.  It is meant to be used across the pre-execution, execution and (as part of the Contract) post-execution lifecycle contexts.
    """
    identifier: List[cdm.base.staticdata.asset.common.ProductIdentifier.ProductIdentifier] = Field([], description="Comprises a identifier and a source to uniquely identify the nonTransferableProduct. ")
    """
    Comprises a identifier and a source to uniquely identify the nonTransferableProduct. 
    """
    taxonomy: List[cdm.base.staticdata.asset.common.ProductTaxonomy.ProductTaxonomy] = Field([], description="Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.")
    """
    Specifies the product taxonomy, which is composed of a taxonomy value and a taxonomy source.
    """
    economicTerms: cdm.product.template.EconomicTerms.EconomicTerms = Field(..., description="The price forming features, including payouts and provisions.")
    """
    The price forming features, including payouts and provisions.
    """
    
    @rosetta_condition
    def condition_0_PrimaryAssetClass(self):
        """
        Specifies that when nonStandardisedTerms are True that a primary asset class must be specified.
        """
        item = self
        def _then_fn0():
            return rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(self, "taxonomy"), "primaryAssetClass"))
        
        def _else_fn0():
            return True
        
        return if_cond_fn(all_elements(rosetta_resolve_attr(rosetta_resolve_attr(self, "economicTerms"), "nonStandardisedTerms"), "=", True), _then_fn0, _else_fn0)

import cdm 
import cdm.base.staticdata.asset.common.ProductIdentifier
import cdm.base.staticdata.asset.common.ProductTaxonomy
import cdm.product.template.EconomicTerms
