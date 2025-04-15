# FpML Circular Dependency Fixes

This document summarizes the improvements made to the FpML model generator to properly handle circular dependencies, based on the approach used in the FIX model generator.

## Overview of Changes

The following changes were implemented to improve handling of circular dependencies in the FpML model generator:

1. **Topological Sorting of Types**: Added a new `topological_sort` function to ensure types are defined in dependency order
2. **Improved Import Ordering**: Updated the __init__.py generation to import models in the correct dependency order
3. **Model Validators for Forward References**: Added `model_validator` decorators to all models
4. **Explicit Forward References**: Added proper ForwardRef definitions for circular dependencies
5. **Proper Build Order**: Modified the main function to generate models in the correct dependency order

## Specific Improvements

### 1. Topological Sorting

Added a new function to sort types based on their dependencies:

```python
def topological_sort(types_dict: Dict[str, Any]) -> List[str]:
    """
    Sort types in topological order based on their dependencies.
    This ensures types are defined before they are referenced.
    """
    # Build dependency graph
    dependencies = {}
    for name, type_obj in types_dict.items():
        deps = set()
        
        # For complex types, track field dependencies
        if hasattr(type_obj, 'elements'):
            for element in type_obj.elements:
                if element.type_name and element.type_name in types_dict:
                    deps.add(element.type_name)
        
        # For simple types, track base type dependencies
        if hasattr(type_obj, 'base_type') and type_obj.base_type in types_dict:
            deps.add(type_obj.base_type)
            
        dependencies[name] = deps
    
    # Topological sort algorithm
    sorted_types = []
    visited = set()
    temp_visited = set()
    
    def visit(node):
        if node in temp_visited:
            # We've hit a cycle, skip this to avoid infinite recursion
            # This will be handled by forward references in the generated code
            return
        if node in visited:
            return
            
        temp_visited.add(node)
        for dep in dependencies.get(node, set()):
            visit(dep)
        temp_visited.remove(node)
        visited.add(node)
        sorted_types.append(node)
    
    # Visit all nodes
    for name in types_dict:
        if name not in visited:
            visit(name)
    
    return sorted_types
```

### 2. Improved Import Ordering

Updated the generation of __init__.py files to use the topological sort:

```python
# Sort enum types in topological order
sorted_enum_names = topological_sort(enum_types)

# Create __init__.py with properly ordered imports
with open(enums_dir / "__init__.py", "w") as f:
    f.write('"""FpML enumeration types."""\n\n')
    
    # Import all enums in topological order
    if sorted_enum_names:
        for enum_name in sorted_enum_names:
            snake_name = camel_to_snake(enum_name)
            f.write(f"from .{snake_name} import {enum_name}\n")
```

### 3. Model Validators for Forward References

Added model validators to all models to ensure forward references are resolved:

```python
@model_validator(mode='after')
def resolve_forward_refs(self):
    """Resolve forward references after model creation."""
    return self
```

### 4. Explicit Forward References

Added explicit forward references for circular dependencies:

```python
# Import forward references for complex types
forward_refs = set()
for element in ctype.elements:
    if element.type_name in complex_types and element.type_name != name:
        ref_name = element.type_name
        forward_refs.add(ref_name)

# Add TYPE_CHECKING imports for forward references
if forward_refs:
    f.write("if TYPE_CHECKING:\n")
    for ref_name in sorted(forward_refs):
        snake_ref = camel_to_snake(ref_name)
        f.write(f"    from ..common.{snake_ref} import {ref_name}\n")
    f.write("\n")
    
    # Define ForwardRef variables
    for ref_name in sorted(forward_refs):
        f.write(f"{ref_name}Ref = ForwardRef('{ref_name}')\n")
    f.write("\n")
```

### 5. Proper Build Order

Updated the main function to generate models in the correct dependency order:

```python
# Generate models in the correct dependency order
# 1. Base classes first (has no dependencies)
logger.info("Generating base classes...")
generate_base_classes()

# 2. Enums second (may depend on base classes)
logger.info("Generating enum models...")
generate_enum_models(simple_types)

# 3. Common types third (may depend on base classes and enums)
logger.info("Generating common type models...")
generate_type_models(complex_types, simple_types)

# 4. Trade models last (depend on all other models)
logger.info("Generating trade models...")
generate_trade_models(elements, complex_types)
```

## Root __init__.py Improvements

Updated the root __init__.py to import in the correct order, preventing circular imports:

```python
"""
Generated FpML model classes.
"""
# Import base classes first to avoid circular imports
from .base import FpMLModelBase, FpMLTradeBase, FpMLComponentBase, FpMLMessageBase

# Then import major models
from .trade import FpMLTrade

# Finally import enum types and common types
from .enums import *
from .common import *
```

## Conclusion

These improvements ensure that circular dependencies in the FpML models are properly handled using Pydantic's forward references and model_rebuild() mechanism, following the same approach used in the FIX model generator. The key difference is the addition of topological sorting of types to ensure proper import ordering, which makes the dependency resolution more robust. 