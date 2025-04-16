# CDM Trade Repository POC

This project is a proof of concept for a trade repository using the Common Domain Model (CDM) and FIX protocol.

## Features

- FIX 4.4 Pydantic model generator
- Automatic generation of Python models from FIX specification
- Support for all FIX 4.4 messages, components, and fields
- Proper handling of repeating groups and nested components
- Type-safe field validation using Pydantic

## Project Structure

```
.
├── src/
│   ├── generators/           # Code generation tools
│   │   ├── fix_spec_downloader.py  # Downloads and parses FIX spec
│   │   └── fix_model_generator.py  # Generates Pydantic models
│   └── models/              # Generated models
│       └── fix/            # FIX protocol models
│           └── generated/  # Auto-generated FIX models
├── specifications/         # FIX specifications
│   └── fix/              # FIX protocol specs
└── tests/                # Test suite
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/yourusername/cdm_trade_repository_poc.git
cd cdm_trade_repository_poc
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Generate FIX models:
```bash
PYTHONPATH=/path/to/project python src/generators/fix_model_generator.py
```

## Usage

The generated models can be used to serialize and deserialize FIX messages:

```python
from src.models.fix.generated.messages.bidresponse import BidResponse
from datetime import datetime

# Create a bid response
bid = BidResponse(
    BeginString="FIX.4.4",
    MsgType="l",
    SenderCompID="SENDER",
    TargetCompID="TARGET",
    MsgSeqNum=1,
    SendingTime=datetime.utcnow(),
    BidID="BID123",
    ClientBidID="CLIENT456"
)

# Serialize to JSON
json_data = bid.model_dump_json()

# Deserialize from JSON
bid_from_json = BidResponse.model_validate_json(json_data)
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## CDM Database Implementation

This project now includes a comprehensive database implementation for storing CDM models:

### Overview
- Database schema design for storing complex CDM models, focusing on Credit Default Swaps
- DAO (Data Access Object) layer for persisting and retrieving CDM trade objects
- Transaction management and circular dependency resolution
- Complete support for the CDM trade model structure

### Key Components
- `src/dao/cdm/schema.sql`: Database schema for CDM models
- `src/dao/cdm/db_manager.py`: Connection management and pooling
- `src/dao/cdm/base_dao.py`: Base Data Access Object implementation
- `src/dao/cdm/cds_dao.py`: Credit Default Swap-specific DAO
- `tests/dao/test_cds_dao.py`: Tests for CDS DAO implementation
- `docs/CDM_DATABASE_DESIGN.md`: Comprehensive documentation

### Database Setup
To initialize the database:

```bash
# Create the database and schema
python -m src.dao.cdm.initialize_db
```

### Using the DAO Layer
```python
from src.dao.cdm.cds_dao import CreditDefaultSwapDAO

# Parse a CDM message into an object
cdm_trade = parser.parse_message(cdm_message_str, 'CDM')

# Initialize CDS DAO
cds_dao = CreditDefaultSwapDAO()

# Save the trade to database
trade_id = cds_dao.save(cdm_trade)

# Retrieve CDS trade details
trade_details = cds_dao.get_comprehensive_details(trade_id)
```

For more information, see the detailed documentation in `docs/CDM_DATABASE_DESIGN.md`. 