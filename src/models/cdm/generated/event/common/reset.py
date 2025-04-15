from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.reference_with_meta_observation import ReferenceWithMetaObservation
    from src.models.cdm.generated.observable.asset.price import Price
    from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation

class Reset(CdmModelBase):
    """Defines the reset value or fixing value produced in cashflow calculations, during the life-cycle of a financial instrument. The reset process defined in Create_Reset function joins product definition details with observations to compute the reset value."""
    reset_value: ForwardRef("Price") = Field(description="Specifies the reset or fixing value. The fixing value could be a cash price, interest rate, or other value.")
    reset_date: str = Field(description="Specifies the date on which the reset occurred.")
    rate_record_date: str = Field(None, description="Specifies the 'Rate Record Day' for a Fallback rate.  Fallback rate fixing processes typically set the fixing rate in arrears, i.e., the Fallback Rate corresponding to a Rate Record Date is set at the end of the interest accural period.  When this applies, Reset->resetDate occurs at the end of the interest period, and the Reset->rateRecordDate occurs near the start of the interest period.  The Reset->rateRecordDate and Reset->observations->observationIdentifier->observationDate will differ if a Fallback rate is unavailable on the Rate Record Date, and the latest previous available rate is used as the observation.")
    observations: List[ForwardRef("ReferenceWithMetaObservation")] = Field(None, description="Represents an audit of the observations used to produce the reset value. If multiple observations were necessary to produce the reset value, the aggregation method should be defined on the payout.")
    averaging_methodology: ForwardRef("AveragingCalculation") = Field(None, description="Identifies the aggregation method to use in the case where multiple observations are used to compute the reset value and the method is not defined in a payout.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.reference_with_meta_observation import ReferenceWithMetaObservation
from src.models.cdm.generated.observable.asset.price import Price
from src.models.cdm.generated.product.template.averaging_calculation import AveragingCalculation
Reset.model_rebuild()
