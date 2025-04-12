
from .base import FIXFieldBase
from .types import FIXInt

class EncryptMethod(FIXFieldBase):
    """FIX EncryptMethod field."""
    tag: str = "98"
    name: str = "EncryptMethod"
    type: str = "INT"
    value: FIXInt

    # Enum values
    # 0: NONE
    # 1: PKCS
    # 2: DES
    # 3: PKCSDES
    # 4: PGPDES
    # 5: PGPDESMD5
    # 6: PEM
