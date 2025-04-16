from dataclasses import dataclass
from typing import Dict, List, Optional
from datetime import datetime

@dataclass
class MappingStats:
    """Class for tracking mapping statistics."""
    total_fields: int = 0
    mapped_fields: int = 0
    unmapped_fields: int = 0
    field_mapping_details: Dict[str, str] = None
    errors: List[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None

    def __init__(self):
        self.field_mapping_details = {}
        self.errors = []
        self.start_time = None
        self.end_time = None

    def start_mapping(self):
        """Start tracking mapping time."""
        self.start_time = datetime.now()

    def end_mapping(self):
        """End tracking mapping time."""
        self.end_time = datetime.now()

    def add_mapped_field(self, field_name: str, mapping_details: str):
        """Record a successfully mapped field."""
        self.total_fields += 1
        self.mapped_fields += 1
        self.field_mapping_details[field_name] = mapping_details

    def add_unmapped_field(self, field_name: str, reason: str):
        """Record an unmapped field."""
        self.total_fields += 1
        self.unmapped_fields += 1
        self.field_mapping_details[field_name] = f"Unmapped: {reason}"

    def add_error(self, error_message: str):
        """Record a mapping error."""
        self.errors.append(error_message)

    def get_summary(self) -> Dict[str, any]:
        """Get a summary of the mapping statistics."""
        duration = None
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds()

        return {
            "total_fields": self.total_fields,
            "mapped_fields": self.mapped_fields,
            "unmapped_fields": self.unmapped_fields,
            "mapping_success_rate": (self.mapped_fields / self.total_fields * 100) if self.total_fields > 0 else 0,
            "field_mapping_details": self.field_mapping_details,
            "errors": self.errors,
            "duration_seconds": duration
        } 