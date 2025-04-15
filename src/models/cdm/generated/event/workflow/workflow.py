from datetime import date, datetime, time
from pydantic import Field, model_validator
from src.models.cdm.generated.base.base import CdmModelBase
from typing import Dict, List, Optional, Any, Union, ForwardRef, TYPE_CHECKING, ClassVar

if TYPE_CHECKING:
    from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep

class Workflow(CdmModelBase):
    """A collection of workflow steps which together makeup an entire workflow sequence."""
    steps: List[ForwardRef("WorkflowStep")] = Field(None)

# Import after class definition to avoid circular imports
from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep
Workflow.model_rebuild()
