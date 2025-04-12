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

__all__ = ['Collateral']


class Collateral(BaseDataClass):
    """
    A type for defining the obligations of the counterparty subject to credit support requirements.
    """
    independentAmount: Optional[cdm.product.collateral.IndependentAmount.IndependentAmount] = Field(None, description="Independent Amount is an amount that usually less creditworthy counterparties are asked to provide. It can either be a fixed amount or a percentage of the Transaction's value. The Independent Amount can be: (i) transferred before any trading between the parties occurs (as a deposit at a third party's account or with the counterparty) or (ii) callable after trading has occurred (typically because a downgrade has occurred). In situation (i), the Independent Amount is not included in the calculation of Exposure, but in situation (ii), it is included in the calculation of Exposure. Thus, for situation (ii), the Independent Amount may be transferred along with any collateral call. Independent Amount is a defined term in the ISDA Credit Support Annex. ('with respect to a party, the amount specified as such for that party in Paragraph 13; if no amount is specified, zero').")
    """
    Independent Amount is an amount that usually less creditworthy counterparties are asked to provide. It can either be a fixed amount or a percentage of the Transaction's value. The Independent Amount can be: (i) transferred before any trading between the parties occurs (as a deposit at a third party's account or with the counterparty) or (ii) callable after trading has occurred (typically because a downgrade has occurred). In situation (i), the Independent Amount is not included in the calculation of Exposure, but in situation (ii), it is included in the calculation of Exposure. Thus, for situation (ii), the Independent Amount may be transferred along with any collateral call. Independent Amount is a defined term in the ISDA Credit Support Annex. ('with respect to a party, the amount specified as such for that party in Paragraph 13; if no amount is specified, zero').
    """
    portfolioIdentifier: List[cdm.base.staticdata.identifier.Identifier.Identifier] = Field([], description="A list of identifiers pointing to the collateral portfolios which contain the collateral which covers a trade.")
    """
    A list of identifiers pointing to the collateral portfolios which contain the collateral which covers a trade.
    """
    collateralPortfolio: List[AttributeWithReference | cdm.event.common.CollateralPortfolio.CollateralPortfolio] = Field([], description="The collateral portfolios which contain the collateral which covers a trade. (NB: this can be provided by reference to a global key for each CollateralPortfolio object)")
    """
    The collateral portfolios which contain the collateral which covers a trade. (NB: this can be provided by reference to a global key for each CollateralPortfolio object)
    """
    collateralProvisions: Optional[cdm.product.collateral.CollateralProvisions.CollateralProvisions] = Field(None, description="specifies the collateral provisions of the product.")
    """
    specifies the collateral provisions of the product.
    """
    
    @rosetta_condition
    def condition_0_CollateralExists(self):
        """
        Collateral must represent either a simple independent amount or full collateral portfolio.
        """
        item = self
        return (rosetta_attr_exists(rosetta_resolve_attr(self, "independentAmount")) or rosetta_attr_exists(rosetta_resolve_attr(self, "collateralPortfolio")))
    
    @rosetta_condition
    def condition_1_CollateralProvisions(self):
        """
        When a collateral portfolio is provided, collateral provisions must exists that govern this collateral.
        """
        item = self
        def _then_fn0():
            return rosetta_attr_exists(rosetta_resolve_attr(self, "collateralProvisions"))
        
        def _else_fn0():
            return True
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "collateralPortfolio")), _then_fn0, _else_fn0)
    
    @rosetta_condition
    def condition_2_Collateralchoice(self):
        item = self
        return rosetta_check_one_of(self, 'independentAmount', 'portfolioIdentifier', 'collateralPortfolio', necessity=False)

import cdm 
import cdm.product.collateral.IndependentAmount
import cdm.base.staticdata.identifier.Identifier
import cdm.event.common.CollateralPortfolio
import cdm.product.collateral.CollateralProvisions
