from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
    from src.models.cdm.generated.metafields.field_with_meta_commodity_business_calendar_enum import FieldWithMetaCommodityBusinessCalendarEnum
    from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters

class BusinessCenters(CdmModelBase):
    """A class for specifying the business day calendar location used in determining whether a day is a business day or not, either by specifying this business center by reference to an enumerated list that is maintained by the FpML standard, or by reference to such specification when it exists elsewhere as part of the instance document. This class corresponds to the FpML BusinessCentersOrReference.model."""
    business_center: List[ForwardRef("FieldWithMetaBusinessCenterEnum")] = Field(None, description="A code identifying one or several business day calendar location(s). The set of business day calendar locations are specified by the business day calendar location enumeration which is maintained by the FpML standard.")
    commodity_business_calendar: List[ForwardRef("FieldWithMetaCommodityBusinessCalendarEnum")] = Field(None)
    business_centers_reference: ForwardRef("ReferenceWithMetaBusinessCenters") = Field(None, description="A reference to a financial business center location specified elsewhere in the instance document.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.metafields.field_with_meta_business_center_enum import FieldWithMetaBusinessCenterEnum
from src.models.cdm.generated.metafields.field_with_meta_commodity_business_calendar_enum import FieldWithMetaCommodityBusinessCalendarEnum
from src.models.cdm.generated.metafields.reference_with_meta_business_centers import ReferenceWithMetaBusinessCenters
BusinessCenters.model_rebuild()
