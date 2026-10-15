import os
import random
import sys
from pathlib import Path
from types import SimpleNamespace

_binary = Path(sys.executable)
_working_dir = Path(os.path.abspath(os.path.dirname(__file__)))

CONFIG: SimpleNamespace = SimpleNamespace(
    session=SimpleNamespace(id=str(random.getrandbits(32))),
    paths=SimpleNamespace(
        bin=Path(_binary),
        build=Path(f"{_working_dir}/out/build"),
        logs=Path(f"{_working_dir}/logs"),
    ),
)
