from contextlib import contextmanager
from typing import Type, List

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.tables import Record, Table


class DatabaseSqlite:

    def __init__(self, db_path):
        self._db_path = db_path
        self._engine = None
        self._backup = None

    def create_tables(self, *tables: Table):
        for table in tables:
            table.get_table().create(self.engine)

    def tables_is_exists(self, *tables: Table) -> bool:
        for table in tables:
            if not table.get_table().exists(self.engine):
                return False
        return True

    def insert_record(self, record: Record):
        with self.session as session:
            session.add(record)

    def select_all(self, table: Type[Record], **filter_by) -> List[Record]:
        with self.session as session:
            return session.query(table).filter_by(**filter_by).all()

    def select(self, table: Type[Record], **filter_by) -> Record:
        with self.session as session:
            row = session.query(table).filter_by(**filter_by).first()
            if row is None:
                raise Exception('В таблице отсутствуют данные')
            return row

    def update(self, table: Table, data: dict, **filter_by):
        with self.session as session:
            session.query(table).filter_by(**filter_by).update(data)

    def _create_db(self):
        self._engine = create_engine(f'sqlite:///{self._db_path}', echo=False)

    @property
    def engine(self):
        if self._engine:
            return self._engine
        self._create_db()
        return self._engine

    @property
    @contextmanager
    def session(self):
        session = sessionmaker(bind=self.engine)(expire_on_commit=False)
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
