import random
import sys
from pathlib import Path

DATABASE_PATH = Path(sys.path[0], 'utils', 'Warship.sqlite')
DATABASE_BACKUP_PATH = Path(sys.path[0], 'utils', 'Warship_backup.sqlite')

SHIPS_MAX = 200
WEAPONS_MAX = 20
HULLS_MAX = 5
ENGINES_MAX = 6


def get_parameter_value() -> int:
    return random.randint(1, 20)
