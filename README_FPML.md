# FpML Model Generator and Parser

This document explains how to use the FpML model generator to create Pydantic models from FpML schema files, and how to parse FpML messages using these models.

## Overview

The FpML model generator consists of:

1. **Schema Downloader**: Downloads FpML schema definitions (XSD files) from the official FpML site
2. **Model Generator**: Parses FpML schemas and generates Pydantic models
3. **Parser**: Parses FpML XML messages into the generated Pydantic models

## Step 1: Download FpML Schemas

First, download the FpML schemas:

```bash
python -m src.generators.fpml_schema_downloader
```

This will download the default FpML 5.10 schemas. To download a different version:

```bash
python -m src.generators.fpml_schema_downloader --version 5-9
```

Available versions: 5-10, 5-9, 5-8, 5-7, 5-6

## Step 2: Generate Pydantic Models

Generate the Pydantic models from the downloaded schemas:

```bash
python -m src.generators.fpml_model_generator
```

To generate models for a specific version:

```bash
python -m src.generators.fpml_model_generator --version 5-9
```

To force regeneration of models:

```bash
python -m src.generators.fpml_model_generator --force
```

## Step 3: Parse FpML Messages

Once the models are generated, you can use them to parse FpML messages:

```python
from src.parsers.controller import ParserController

# Create the parser controller
controller = ParserController()

# Example FpML message
fpml_message = """
<FpML xmlns="http://www.fpml.org/FpML-5/confirmation">
  <trade>
    <tradeHeader>
      <partyTradeIdentifier>
        <partyReference href="Party1"/>
        <tradeId>TRADE123</tradeId>
      </partyTradeIdentifier>
      <tradeDate>2024-04-12</tradeDate>
    </tradeHeader>
    <!-- ... -->
  </trade>
</FpML>
"""

# Parse the message
async def parse():
    trade = await controller.parse_message(fpml_message, 'FPML')
    print(f"Parsed trade: {trade}")
    print(f"Trade ID: {trade.tradeHeader.partyTradeIdentifier[0].tradeId}")
    return trade

# Run the async function
import asyncio
trade = asyncio.run(parse())
```

## Generated Model Structure

The generated models are organized as follows:

```
/src/models/fpml/generated/
├── __init__.py
├── base
│   ├── __init__.py
│   └── base.py  (FpMLModelBase, FpMLTradeBase, etc.)
├── enums
│   ├── __init__.py
│   └── (enum classes)
├── common
│   ├── __init__.py
│   └── (common type classes)
├── components
│   ├── __init__.py
│   └── (component classes)
├── messages
│   ├── __init__.py
│   └── (message classes)
└── trade
    ├── __init__.py
    └── trade.py (FpMLTrade)
```

## Running Tests

To run the FpML tests:

```bash
pytest tests/test_fpml_irs_message.py
pytest tests/test_fpml_cds_message.py
```

## Extending the Models

To extend the generated models, create subclasses in your application code:

```python
from src.models.fpml.generated.trade import FpMLTrade

class EnhancedFpMLTrade(FpMLTrade):
    def calculate_npv(self):
        # Custom business logic
        return 0.0
```

## Handling Circular Dependencies

The generated models use Pydantic's `model_rebuild()` mechanism to handle circular dependencies. This is handled automatically in the generated code. 