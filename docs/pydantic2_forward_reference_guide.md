# Forward References in Pydantic 2

This guide explains how to use forward references in Pydantic 2 to handle circular dependencies between models.

## Key Differences from Pydantic 1

In Pydantic 2, the handling of forward references has changed:

1. `update_forward_refs()` is deprecated and replaced with `model_rebuild()`
2. A model validator can be used to ensure references are resolved
3. The string literal forward references still work as before

## Example Usage

Here's how to properly use forward references in Pydantic 2:

```python
from typing import Optional, List, ForwardRef, TYPE_CHECKING
from pydantic import BaseModel, Field, ConfigDict, model_validator, model_rebuild

# For IDE type hints
if TYPE_CHECKING:
    from .other_model import OtherModel

# Define forward reference outside the class
OtherModelRef = ForwardRef('OtherModel')

class MyModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    
    name: str
    other: Optional[OtherModelRef] = None
    
    # Optional: Add a model validator to handle forward references
    @model_validator(mode='after')
    def resolve_forward_refs(self):
        return self

# Make sure to call model_rebuild() after all models are defined
MyModel.model_rebuild()
```

## Handling Circular Imports

When you have circular imports between modules, use this pattern:

1. Use the `TYPE_CHECKING` guard for import statements
2. Define forward references outside the class
3. Use the forward references in your model
4. Call `model_rebuild()` after all models are defined
5. Optionally add a model validator to ensure references are resolved

## Generated FIX Model Changes

In our FIX model generator, we've updated the code to:

1. Import `model_rebuild` from Pydantic 
2. Replace calls to `update_forward_refs()` with `model_rebuild()`
3. Add a model validator to properly handle forward references
4. Use type checking imports to provide better IDE support

### Example of Generated Component

```python
from typing import List, Optional, ForwardRef, TYPE_CHECKING
from pydantic import Field, ConfigDict, model_rebuild, model_validator
from .base import FIXComponentBase

if TYPE_CHECKING:
    from ..components.parties import PartiesComponent

# Forward references for components to avoid circular imports
PartiesComponent = ForwardRef('PartiesComponent')

class OrderComponent(FIXComponentBase):
    """Order Component"""

    model_config = ConfigDict(populate_by_name=True)

    OrderID: str = Field(..., alias="37", description="Order ID")
    Parties: Optional[PartiesComponent] = Field(None, description="Parties component")
    
    @model_validator(mode='after')
    def resolve_forward_refs(self):
        return self

# Rebuild models to resolve forward references
OrderComponent.model_rebuild()
PartiesComponent.model_rebuild()
```

## Testing Forward References

You can test that forward references are working correctly by:

1. Creating instances of your models
2. Setting up circular references between them
3. Accessing properties through the circular references
4. Serializing models with circular references 

See the test script at `src/generators/test_pydantic2_forwards.py` for a complete example. 