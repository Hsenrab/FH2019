# This must be at the top of all clients

import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.as_posix()
sys.path.append(ROOT)