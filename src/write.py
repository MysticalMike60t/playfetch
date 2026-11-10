from pathlib import Path

from config import CONFIG


def extracted(local_path: str | Path, content: str):
    if isinstance(local_path, Path):
        local_path: str = str(local_path)

    Path(CONFIG.paths.tmp).mkdir(exist_ok=True)
    with open(f"{CONFIG.paths.tmp}/{local_path}", "w") as f:
        _ = f.write(content)
