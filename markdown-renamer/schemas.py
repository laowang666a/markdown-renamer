from dataclasses import dataclass
from pathlib import Path

@dataclass
class RenameJob:
    file_path: Path
    new_name: str
    status: str = "pending"