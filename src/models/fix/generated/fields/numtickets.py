
from .base import FIXFieldBase
from .types import FIXInt

class NumTickets(FIXFieldBase):
    """FIX NumTickets field."""
    tag: str = "395"
    name: str = "NumTickets"
    type: str = "INT"
    value: FIXInt
