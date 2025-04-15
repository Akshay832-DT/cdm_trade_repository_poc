from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.legaldocumentation.common.resource_length import ResourceLength
    from src.models.cdm.generated.metafields.field_with_meta_resource_type_enum import FieldWithMetaResourceTypeEnum
    from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString

class Resource(CdmModelBase):
    """Describes the resource that contains the media representation of a business event (i.e used for stating the Publicly Available Information). For example, can describe a file or a URL that represents the event. This type is an extended version of a type defined by RIXML (www.rixml.org).  Rosetta restricts the FpML implementation by not providing the ability to associated a document in hexadecimalBinary or base64Binary until such time that actual use cases will come up."""
    resource_id: ForwardRef("FieldWithMetaString") = Field(description="The unique identifier of the resource within the event. FpML specifies this element of type resourceIdScheme but with no specified value.")
    resource_type: ForwardRef("FieldWithMetaResourceTypeEnum") = Field(None, description="A description of the type of the resource, e.g. a confirmation.")
    language: ForwardRef("FieldWithMetaString") = Field(None, description="Indicates the language of the resource, described using the ISO 639-2/T Code.")
    size_in_bytes: float = Field(None, description="Indicates the size of the resource in bytes. It could be used by the end user to estimate the download time and storage needs.")
    length: ForwardRef("ResourceLength") = Field(None, description="Indicates the length of the resource. For example, if the resource were a PDF file, the length would be in pages.")
    mime_type: ForwardRef("FieldWithMetaString") = Field(None, description="Indicates the type of media used to store the content. mimeType is used to determine the software product(s) that can read the content. MIME Types are described in RFC 2046.")
    name: str = Field(None, description="The name of the resource.  It is specified as a NormalizedString in FpML.")
    comments: str = Field(None, description="Any additional comments that are deemed necessary. For example, which software version is required to open the document? Or, how does this resource relate to the others for this event?")
    string: str = Field(None, description="Provides extra information as string. In case the extra information is in XML format, a CDATA section must be placed around the source message to prevent its interpretation as XML content.")
    url: str = Field(None, description="Indicates where the resource can be found, as a URL that references the information on a web server accessible to the message recipient.")

# Import after class definition to avoid circular imports
from src.models.cdm.generated.legaldocumentation.common.resource_length import ResourceLength
from src.models.cdm.generated.metafields.field_with_meta_resource_type_enum import FieldWithMetaResourceTypeEnum
from src.models.cdm.generated.metafields.field_with_meta_string import FieldWithMetaString
Resource.model_rebuild()
