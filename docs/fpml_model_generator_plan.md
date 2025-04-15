# FpML Model Generator Implementation Plan

## Overview
This document outlines the plan to implement an FpML model generator that creates Pydantic models from FpML specifications, similar to the existing FIX model generator.

## Components to Develop

1. **FpML Schema Downloader**
   - Download FpML schema definitions (XSD files) from the official FpML site
   - Store in specifications/fpml/ directory
   - Cache downloaded schemas

2. **FpML Model Generator**
   - Parse FpML XSD schemas to extract data structures
   - Generate Pydantic models for FpML types, elements, and messages
   - Handle circular dependencies using Pydantic's forward references
   - Output generated models to src/models/fpml/generated/

3. **FpML Parser Implementation**
   - Update the existing FpML parser to use generated models
   - Map XML elements to generated Pydantic models

4. **Tests**
   - Create test cases for IRS and CDS FpML messages
   - Test parsing and validation functionality

## Implementation Steps

### Step 1: Create FpML Schema Downloader
- Create a script in src/generators/fpml_schema_downloader.py
- Download and save FpML schema files for the required version (FpML 5.x)
- Implement caching to avoid redundant downloads

### Step 2: Create FpML Model Generator
- Create src/generators/fpml_model_generator.py
- Implement schema parsing for XSD files
- Handle complex type definitions, elements, attributes, and extensions
- Handle recursive/circular references with Pydantic's model_rebuild()
- Generate models in a hierarchical structure similar to FIX

### Step 3: Generate Model Directory Structure
- Create a structure similar to the FIX model directory:
  ```
  /src/models/fpml/generated/
  ├── __init__.py
  ├── base.py
  ├── types.py
  ├── common/
  ├── components/
  ├── messages/
  └── trade/
  ```

### Step 4: Update FpML Parser
- Update src/parsers/fpml/parser.py to use the generated models
- Enhance validation and parsing functionality
- Ensure proper mapping from XML to model structures

### Step 5: Create Tests for IRS and CDS
- Create tests/test_fpml_irs_message.py
- Create tests/test_fpml_cds_message.py
- Test validation, parsing, and model interaction

## Key Challenges and Solutions

### Circular Dependencies
- Use ForwardRef and model_rebuild() similar to the FIX implementation
- Implement TYPE_CHECKING pattern for imports

### Complex XSD Schemas
- Implement proper handling of XSD schema imports and includes
- Handle namespaces correctly
- Handle XML Schema complexType, simpleType, element, and attribute definitions

### Test Data
- Create sample FpML messages for IRS and CDS based on FpML specifications
- Store these in tests/data/fpml/ directory

## Development Timeline

1. Schema Downloader - 1 day
2. Basic Model Generator - 2 days
3. Complex Type Handling - 1 day
4. Circular Reference Resolution - 1 day
5. Parser Updates - 1 day
6. Test Creation - 1 day

Total estimated time: 7 days

## Success Criteria

1. FpML model generator creates valid Pydantic models from FpML schemas
2. FpML parser correctly parses and validates FpML messages
3. All tests pass for IRS and CDS FpML messages
4. Generated models handle circular references properly
5. Parser correctly maps XML to model structures 