#!/usr/bin/env python3
import sys
print("Python path:", sys.path)

try:
    from models.fix.generated.components.instrument import InstrumentComponent
    print("Successfully imported InstrumentComponent")
    
    instrument = InstrumentComponent(
        Symbol="AAPL",
        SecurityID="037833100",
        SecurityIDSource="1"
    )
    print(f"Created instrument: {instrument}")
    print("Test passed!")
except ImportError as e:
    print(f"Import error: {e}")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc() 