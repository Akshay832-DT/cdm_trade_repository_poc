#!/usr/bin/env python
"""
Test for Pydantic forward references
"""
from typing import Optional, List, ForwardRef
from pydantic import BaseModel

# Define a model with a forward reference
class TestModel(BaseModel):
    name: str
    value: int
    related: Optional['RelatedModel'] = None

class RelatedModel(BaseModel):
    id: str
    description: str
    parent: Optional[TestModel] = None

# Update forward references
TestModel.update_forward_refs()
RelatedModel.update_forward_refs()

# Create instances
test = TestModel(name="Test", value=123)
related = RelatedModel(id="R1", description="Related item")

# Set up circular reference
test.related = related
related.parent = test

print(f"Created test model: {test}")
print(f"With related model: {test.related}")
print(f"Circular reference: {test.related.parent is test}")

# Test serialization
test_dict = test.dict()
print(f"Serialized: {test_dict}")

print("Test completed successfully!") 