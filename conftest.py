import pytest

from database.database_operations import DatabaseWarship
from database.tables import Weapons, Hulls, Engines, Ships
from utils.util import DATABASE_PATH


@pytest.fixture(scope='session')
def backup_and_random_current_db():
    db = DatabaseWarship(DATABASE_PATH)
    db.backup()

    for ship in db.ships:
        db.update(Ships, Ships.change_random_attr(), ship=ship.ship)

    for weapon in db.weapons:
        db.update(Weapons, Weapons.change_random_attr(), weapon=weapon.weapon)

    for hull in db.hulls:
        db.update(Hulls, Hulls.change_random_attr(), hull=hull.hull)

    for engine in db.engines:
        db.update(Engines, Engines.change_random_attr(), engine=engine.engine)
