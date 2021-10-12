import random
import sqlite3
from typing import List

from faker import Faker

from database.database_common import DatabaseSqlite
from database.tables import Weapons, Hulls, Engines, Ships
from utils.util import DATABASE_PATH, DATABASE_BACKUP_PATH, SHIPS_MAX, WEAPONS_MAX, HULLS_MAX, ENGINES_MAX, \
    get_parameter_value


class DatabaseWarship(DatabaseSqlite):

    def __init__(self, db_path=DATABASE_PATH):
        super().__init__(db_path=db_path)
        self._fill_database_random_data()

    def backup(self):
        self._backup = sqlite3.connect(DATABASE_BACKUP_PATH)
        main_db_connect = sqlite3.connect(self._db_path)
        main_db_connect.backup(self._backup)

    def add_weapon(self, weapon: Weapons):
        self.insert_record(weapon)

    def add_hull(self, hull: Hulls):
        self.insert_record(hull)

    def add_engine(self, engine: Engines):
        self.insert_record(engine)

    def add_ship(self, ship: Ships):
        self.insert_record(ship)

    def get_ship_by_name(self, name: str) -> Ships:
        ship = self.select(Ships, ship=name)
        return Ships(
            ship=ship.ship,
            weapon=ship.weapon,
            hull=ship.hull,
            engine=ship.engine
        )

    def get_weapon_by_name(self, name: str) -> Weapons:
        weapon = self.select(Weapons, weapon=name)
        return Weapons(
            weapon=weapon.weapon,
            reload_speed=weapon.reload_speed,
            rotation_speed=weapon.rotation_speed,
            diameter=weapon.diameter,
            power_volley=weapon.power_volley,
            count=weapon.count
        )

    def get_hull_by_name(self, name: str) -> Hulls:
        hull = self.select(Hulls, hull=name)
        return Hulls(
            hull=hull.hull,
            armor=hull.armor,
            type=hull.type,
            capacity=hull.capacity
        )

    def get_engine_by_name(self, name: str) -> Engines:
        engine = self.select(Engines, engine=name)
        return Engines(
            engine=engine.engine,
            power=engine.power,
            type=engine.type
        )

    @property
    def ships(self) -> List[Ships]:
        return self.select_all(Ships)

    @property
    def weapons(self) -> List[Weapons]:
        return self.select_all(Weapons)

    @property
    def hulls(self) -> List[Hulls]:
        return self.select_all(Hulls)

    @property
    def engines(self) -> List[Engines]:
        return self.select_all(Engines)

    def _fill_database_random_data(self):
        if not self.tables_is_exists(Weapons, Hulls, Engines, Ships):
            self.create_tables(Weapons, Hulls, Engines, Ships)

            for i in range(WEAPONS_MAX):
                weapon = Weapons(
                    weapon=f'Weapon-{i}',
                    reload_speed=get_parameter_value(),
                    rotation_speed=get_parameter_value(),
                    diameter=get_parameter_value(),
                    power_volley=get_parameter_value(),
                    count=get_parameter_value()
                )
                self.add_weapon(weapon)

            for i in range(HULLS_MAX):
                hull = Hulls(
                    hull=f'Hull-{i}',
                    armor=get_parameter_value(),
                    type=get_parameter_value(),
                    capacity=get_parameter_value()
                )
                self.add_hull(hull)

            for i in range(ENGINES_MAX):
                engine = Engines(
                    engine=f'Engine-{i}',
                    power=get_parameter_value(),
                    type=get_parameter_value()
                )
                self.add_engine(engine)

            faker = Faker('RU')
            for i in range(SHIPS_MAX):
                ship = Ships(
                    ship=f'Ship-{faker.unique.first_name()}',
                    weapon=f'Weapon-{random.randint(1, WEAPONS_MAX)}',
                    hull=f'Hull-{random.randint(1, HULLS_MAX)}',
                    engine=f'Engine-{random.randint(1, ENGINES_MAX)}'
                )
                self.add_ship(ship)
