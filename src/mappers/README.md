# CDM Trade Mappers

This package provides a framework for mapping between different financial data formats (FIX, FpML) and the Common Domain Model (CDM).

## Overview

The mapper implementation is designed to be:

- **Configurable**: Most mappings are defined in YAML configuration files
- **Extensible**: Easy to add new mappers for different message types
- **Traceable**: Tracks mapping statistics and generates reports
- **Modular**: Clear separation between different components

## Structure

- `base.py`: Base mapper classes and common functionality
- `controller.py`: Controller for selecting appropriate mappers
- `config/`: YAML configuration files for mappings
  - `fix/`: FIX to CDM mapping configurations
  - `fpml/`: FPML to CDM mapping configurations
- `fix/`: FIX to CDM mappers
- `fpml/`: FPML to CDM mappers
- `utils/`: Utility classes and functions
  - `mapping_tracker.py`: Tracks mapping statistics
  - `transformers.py`: Data transformation utilities

## Mapping Configuration

Mappings are defined in YAML files with a standard structure:

```yaml
metadata:
  source_type: "ExecutionReport"
  target_type: "WorkflowStep"
  description: "Maps FIX ExecutionReport to CDM WorkflowStep"
  version: "1.0"

mappings:
  - source_field: "ClOrdID"
    target_field: "business_event.trade.party_trade_information[0].trade_id.identifier.value"
    description: "Maps client order ID to trade identifier"
    transformer: "direct"
  
  # More mappings...
```

## Available Transformers

The following transformers are available:

- `direct`: Direct mapping without transformation
- `date_format`: Date format transformation
- `enum_map`: Enum mapping transformation
- `bool_transform`: Boolean transformation
- `number_transform`: Number transformation
- `string_transform`: String transformation
- `custom`: Custom transformations (implemented in subclasses)

## FIX Mappers

Currently implemented FIX mappers:

- `ExecutionReportMapper`: Maps FIX ExecutionReport to CDM WorkflowStep

## FPML Mappers

Currently implemented FPML mappers:

- `FpMLTradeMapper`: Maps FPML Trade to CDM WorkflowStep

## Usage

```python
from src.mappers.controller import MapperController
from src.models.fix.generated.messages.executionreport import ExecutionReport

# Create mapper controller
controller = MapperController()

# Create FIX execution report
exec_report = ExecutionReport(...)

# Map to CDM
cdm_obj = controller.map_fix_to_cdm(exec_report)

# Get mapping statistics
fix_mapper = controller.get_fix_mapper("ExecutionReport")
stats = fix_mapper.get_mapping_stats()
```

## Mapping Statistics

The mapper framework tracks mapping statistics, including:

- Mapped fields
- Unmapped fields
- Coverage percentage

A comprehensive report can be generated using the `MappingTracker` utility:

```python
from src.mappers.utils.mapping_tracker import MappingTracker

tracker = MappingTracker()
tracker.add_mapping_stats("ExecutionReport", fix_mapper.get_mapping_stats())
tracker.generate_report("report_directory")
```

## Extending the Framework

To add a new mapper:

1. Create a YAML configuration file in `config/fix/` or `config/fpml/`
2. Implement a mapper class in `fix/` or `fpml/`
3. Register the mapper in the appropriate `__init__.py` file

## Examples

See `src/examples/mapper_example.py` for a complete example of using the mappers. 