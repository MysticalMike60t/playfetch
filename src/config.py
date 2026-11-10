import os
import random
import sys
from logging import Formatter
from pathlib import Path
from types import SimpleNamespace

_binary = Path(sys.executable)
_working_dir = Path(os.path.abspath(os.path.dirname(__file__)))

CONFIG: SimpleNamespace = SimpleNamespace(  # Add type defs
    defaults=SimpleNamespace(http_res_content_encoding="utf-8"),
    session=SimpleNamespace(id=str(random.getrandbits(32))),
    paths=SimpleNamespace(
        bin=Path(_binary),
        build=Path(f"{_working_dir}/out/build"),
        logs=Path(f"{_working_dir}/.logs"),
        tmp=Path(f"{_working_dir}/.tmp"),
    ),
    logs=SimpleNamespace(
        format=Formatter("%(asctime)s %(levelname)s: %(message)s", "%H:%M:%S")
    ),
)
