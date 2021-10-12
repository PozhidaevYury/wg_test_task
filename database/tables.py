import random
from typing import Type

from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship, backref

Record = declarative_base()
Table = Type[Record]


class TableNameMixin:

    @classmethod
    def get_name(cls) -> str:
        return getattr(cls, '__tablename__')

    @classmethod
    def get_table(cls):
        return getattr(cls, '__table__')


class Ships(Record, TableNameMixin):
    __tablename__ = 'Ships'

    ship = Column(Text, primary_key=True)
    weapon = Column(Text, ForeignKey('weapons.weapon'), nullable=False)
    hull = Column(Text, ForeignKey('hulls.hull'), nullable=False)
    engine = Column(Text, ForeignKey('engines.engine'), nullable=False)

    weapons_table = relationship('Weapons')
    hulls_table = relationship('Hulls')
    engines_table = relationship('Engines')

    def __init__(self, ship, weapon, hull, engine):
        self.ship = ship
        self.weapon = weapon
        self.hull = hull
        self.engine = engine

    @staticmethod
    def change_random_attr() -> dict:
        name = random.choice(['weapon', 'hull', 'engine'])
        if name == 'weapon':
            return {Ships.weapon: f'Weapon-{random.randint(1, 20)}'}
        elif name == 'hull':
            return {Ships.hull: f'Hull-{random.randint(1, 5)}'}
        elif name == 'engine':
            return {Ships.engine: f'Engine-{random.randint(1, 6)}'}


class Weapons(Record, TableNameMixin):
    __tablename__ = 'weapons'

    weapon = Column(Text, primary_key=True)
    reload_speed = Column(Integer, nullable=False)
    rotation_speed = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    power_volley = Column(Integer, nullable=False)
    count = Column(Integer, nullable=False)

    def __init__(self, weapon, reload_speed, rotation_speed, diameter, power_volley, count):
        self.weapon = weapon
        self.reload_speed = reload_speed
        self.rotation_speed = rotation_speed
        self.diameter = diameter
        self.power_volley = power_volley
        self.count = count

    @staticmethod
    def change_random_attr() -> dict:
        name = random.choice(['reload_speed', 'rotation_speed', 'diameter', 'power_volley', 'count'])
        if name == 'reload_speed':
            return {Weapons.reload_speed: random.randint(1, 20)}
        elif name == 'rotation_speed':
            return {Weapons.rotation_speed: random.randint(1, 20)}
        elif name == 'diameter':
            return {Weapons.diameter: random.randint(1, 20)}
        elif name == 'power_volley':
            return {Weapons.power_volley: random.randint(1, 20)}
        elif name == 'count':
            return {Weapons.count: random.randint(1, 20)}


class Hulls(Record, TableNameMixin):
    __tablename__ = 'hulls'

    hull = Column(Text, primary_key=True)
    armor = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)
    capacity = Column(Integer, nullable=False)

    def __init__(self, hull, armor, type, capacity):
        self.hull = hull
        self.armor = armor
        self.type = type
        self.capacity = capacity

    @staticmethod
    def change_random_attr() -> dict:
        name = random.choice(['armor', 'type', 'capacity'])
        if name == 'armor':
            return {Hulls.armor: random.randint(1, 20)}
        elif name == 'type':
            return {Hulls.type: random.randint(1, 20)}
        elif name == 'capacity':
            return {Hulls.capacity: random.randint(1, 20)}


class Engines(Record, TableNameMixin):
    __tablename__ = 'engines'

    engine = Column(Text, primary_key=True)
    power = Column(Integer, nullable=False)
    type = Column(Integer, nullable=False)

    def __init__(self, engine, power, type):
        self.engine = engine
        self.power = power
        self.type = type

    @staticmethod
    def change_random_attr() -> dict:
        name = random.choice(['power', 'type'])
        if name == 'power':
            return {Engines.power: random.randint(1, 20)}
        elif name == 'type':
            return {Engines.type: random.randint(1, 20)}
