"""ISDA CDM models."""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.cdm.generated.base.staticdata.asset.credit.not_domestic_currency import NotDomesticCurrency
    from src.models.cdm.generated.base.staticdata.asset.credit.obligation_category_enum import ObligationCategoryEnum
    from src.models.cdm.generated.base.staticdata.asset.credit.obligations import Obligations
    from src.models.cdm.generated.base.staticdata.asset.credit.specified_currency import SpecifiedCurrency
