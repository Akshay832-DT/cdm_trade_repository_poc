# ISDA CDM Model Generator and Parser

This document explains how to use the ISDA CDM model generator to create Pydantic models from CDM JSON schema files, and how to parse CDM JSON messages using these models.

## Overview

The ISDA CDM model generator consists of:

1. **Model Generator**: Parses CDM JSON schemas and generates Pydantic models
2. **Parser**: Parses CDM JSON messages into the generated Pydantic models

## Step 1: Generate Pydantic Models

Generate the Pydantic models from the CDM JSON schemas:

```bash
python generate_cdm_models.py
```

Options:
- `--schema-dir`: Specify a different directory containing CDM JSON schemas (default: specifications/cdm_json)
- `--output`: Specify a different output directory for generated models (default: models/cdm/generated)
- `--backup`: Backup existing generated models before generating new ones
- `--no-clean`: Don't clean output directory before generation

## Step 2: Parse CDM Messages

Once the models are generated, you can use them to parse CDM JSON messages:

```python
from src.parsers.controller import ParserController

# Create the parser controller
controller = ParserController()

# Example CDM message
cdm_message = """
{
    "TradableProduct": {
        "product": {
            "TransferableProduct": {
                "economicTerms": {
                    "payout": [
                        {
                            "interestRatePayout": {
                                "rateSpecification": {
                                    "fixedRate": {
                                        "rate": 0.02, 
                                        "dayCountFraction": "ACT/360"
                                    }
                                },
                                "payerReceiver": {
                                    "payer": {
                                        "partyReference": {"href": "Party1"}
                                    },
                                    "receiver": {
                                        "partyReference": {"href": "Party2"}
                                    }
                                }
                            }
                        }
                    ]
                }
            }
        },
        "tradeDate": {
            "value": "2024-04-12"
        }
    }
}
"""

# Parse the message
trade = await controller.parse_message(cdm_message, 'CDM')

# Access the parsed data
print(f"Trade Date: {trade.tradeDate.value}")
print(f"Payer: {trade.product.TransferableProduct.economicTerms.payout[0].interestRatePayout.payerReceiver.payer.partyReference.href}")
```

## Supported CDM Messages

The parser supports various CDM message types including:

1. Interest Rate Swaps (IRS)
2. Credit Default Swaps (CDS)

## Implementation Details

### Directory Structure

```
models/cdm/generated/     # Generated Pydantic models
├── base/                # Base classes
├── product/             # Product models
├── metafields/          # Metafields models
└── [other subdirectories based on CDM structure]
```

### Generator Implementation

The model generator:

1. Parses all JSON schema files from the specifications directory
2. Resolves dependencies between models 
3. Resolves circular references using Pydantic's forward references
4. Generates Python classes with proper typing
5. Creates a hierarchical module structure matching the CDM structure

### Parser Implementation

The CDM parser:

1. Validates JSON message structure
2. Determines the message type
3. Loads the appropriate model class
4. Parses the message into the model instance
5. Returns the parsed model

## Troubleshooting

### Invalid References

If you encounter issues with invalid references, ensure that:

1. All required schema files are present in the specifications directory
2. The CDM message format matches the expected structure

### Circular Dependencies

If you have issues with circular dependencies:
1. Circular dependencies are handled automatically using Pydantic's forward references
2. In some cases, you may need to update the imports in the generated files

## Future Enhancements

Potential future enhancements include:

1. Adding support for more CDM message types
2. Implementing validation rules specific to CDM
3. Adding schema version compatibility checks 