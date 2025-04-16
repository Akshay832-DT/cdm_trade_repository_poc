from typing import Dict, Any, Type, Optional, List
from pydantic import BaseModel
import os
import yaml
import logging
from pathlib import Path

from ..base import BaseMapper
from src.models.fix.generated.base.fix_message import FIXMessage
from src.models.cdm.generated.event.workflow.workflow_step import WorkflowStep

class BaseFIXMapper(BaseMapper):
    """
    Base class for FIX to CDM mappers
    """
    
    def __init__(self, config_file: Optional[str] = None):
        """
        Initialize the FIX mapper
        
        Args:
            config_file: Optional path to YAML configuration file
            If not specified, will look for a config file based on the class name
        """
        if config_file is None:
            # Determine config file path based on class name
            class_name = self.__class__.__name__
            if class_name.endswith('Mapper'):
                # Remove 'Mapper' suffix for the file name
                message_type = class_name[:-6]
                config_file = os.path.join(
                    Path(__file__).parent.parent, 
                    'config', 'fix', 
                    f"{message_type.lower()}.yaml"
                )
        
        super().__init__(config_file)
    
    def map(self, source_obj: FIXMessage) -> WorkflowStep:
        """
        Map FIX message to CDM WorkflowStep
        
        Args:
            source_obj: FIX message to map
            
        Returns:
            CDM WorkflowStep object
        """
        # Create empty CDM WorkflowStep
        workflow_step = WorkflowStep()
        
        # Apply mappings from config
        if 'mappings' in self.config:
            mappings = self.config['mappings']
            self.stats.total_source_fields = len(mappings)
            
            for mapping in mappings:
                source_field = mapping['source_field']
                target_field = mapping['target_field']
                transformer = mapping.get('transformer', 'direct')
                transformer_params = mapping.get('transformer_params', {})
                
                self.apply_field_mapping(
                    source_obj, workflow_step,
                    source_field, target_field,
                    transformer, transformer_params
                )
        
        # Apply custom mappings (to be implemented in subclasses)
        self.apply_custom_mappings(source_obj, workflow_step)
        
        return workflow_step
    
    def apply_custom_mappings(self, source_obj: FIXMessage, target_obj: WorkflowStep) -> None:
        """
        Apply custom mappings that cannot be defined in YAML
        
        This method should be overridden in subclasses to apply custom mappings
        
        Args:
            source_obj: FIX message to map from
            target_obj: CDM object to map to
        """
        pass 