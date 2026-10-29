import sys
from pathlib import Path

# Add lab3 directory to sys.path so playfair can be imported
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from playfair import main  # noqa: E402

__all__ = ["main"]

