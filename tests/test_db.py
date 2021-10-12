import pytest

from database.database_operations import DatabaseWarship
from database.tables import Ships
from utils.util import DATABASE_BACKUP_PATH


@pytest.mark.usefixtures('backup_and_random_current_db')
@pytest.mark.parametrize(
    'backup_ship',
    [*DatabaseWarship().ships]
)
class TestSuiteWarshipDb:

    def test_compare_weapon_tables(self, backup_ship: Ships):
        changed_database = DatabaseWarship()
        changed_ship = changed_database.get_ship_by_name(backup_ship.ship)

        assert backup_ship.weapon == changed_ship.weapon, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'expected {backup_ship.weapon}, was {changed_ship.weapon}'

        backup_database = DatabaseWarship(DATABASE_BACKUP_PATH)
        backup_weapon = backup_database.get_weapon_by_name(backup_ship.weapon)
        changed_weapon = changed_database.get_weapon_by_name(backup_ship.weapon)

        assert backup_weapon.reload_speed == changed_weapon.reload_speed, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'reload_speed: expected {backup_weapon.reload_speed},' \
            f' was {changed_weapon.reload_speed}'

        assert backup_weapon.rotation_speed == changed_weapon.rotation_speed, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'rotation_speed: expected {backup_weapon.rotation_speed},' \
            f' was {changed_weapon.rotation_speed}'

        assert backup_weapon.diameter == changed_weapon.diameter, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'diameter: expected {backup_weapon.diameter},' \
            f' was {changed_weapon.diameter}'

        assert backup_weapon.power_volley == changed_weapon.power_volley, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'power_volley: expected {backup_weapon.power_volley},' \
            f' was {changed_weapon.power_volley}'

        assert backup_weapon.count == changed_weapon.count, \
            f'{changed_ship.ship}, {changed_ship.weapon}\n\t' \
            f'count: expected {backup_weapon.count},' \
            f' was {changed_weapon.count}'

    def test_compare_hull_tables(self, backup_ship: Ships):
        changed_database = DatabaseWarship()
        changed_ship = changed_database.get_ship_by_name(backup_ship.ship)

        assert backup_ship.hull == changed_ship.hull, \
            f'{changed_ship.ship}, {changed_ship.hull}\n\t' \
            f'expected {backup_ship.hull}, was {changed_ship.hull}'

        backup_database = DatabaseWarship(DATABASE_BACKUP_PATH)
        backup_hull = backup_database.get_hull_by_name(backup_ship.hull)
        changed_hull = changed_database.get_hull_by_name(backup_ship.hull)

        assert backup_hull.type == changed_hull.type, \
            f'{changed_ship.ship}, {changed_ship.hull}\n\t' \
            f'count: expected {backup_hull.type},' \
            f' was {changed_hull.type}'

        assert backup_hull.armor == changed_hull.armor, \
            f'{changed_ship.ship}, {changed_ship.hull}\n\t' \
            f'count: expected {backup_hull.armor},' \
            f' was {changed_hull.armor}'

        assert backup_hull.capacity == changed_hull.capacity, \
            f'{changed_ship.ship}, {changed_ship.hull}\n\t' \
            f'count: expected {backup_hull.capacity}' \
            f' was {changed_hull.capacity}'

    def test_compare_engine_tables(self, backup_ship: Ships):
        changed_database = DatabaseWarship()
        changed_ship = changed_database.get_ship_by_name(backup_ship.ship)

        assert backup_ship.engine == changed_ship.engine, \
            f'{changed_ship.ship}, {changed_ship.engine}\n\t' \
            f'expected {backup_ship.engine}, was {changed_ship.engine}'

        backup_database = DatabaseWarship(DATABASE_BACKUP_PATH)
        backup_engine = backup_database.get_engine_by_name(backup_ship.engine)
        changed_engine = changed_database.get_engine_by_name(backup_ship.engine)

        assert backup_engine.type == changed_engine.type, \
            f'{changed_ship.ship}, {changed_ship.engine}\n\t' \
            f'count: expected {backup_engine.type},' \
            f' was {changed_engine.type}'

        assert backup_engine.power == changed_engine.power, \
            f'{changed_ship.ship}, {changed_ship.engine}\n\t' \
            f'count: expected {backup_engine.power},' \
            f' was {changed_engine.power}'
