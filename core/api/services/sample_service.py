from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Union, List

import sqlalchemy
from sqlalchemy import MetaData, Table, Column, String, BigInteger
from sqlalchemy.engine import Engine, create_engine

from config import Configuration
from core.api.services import AbstractService
from utils import Logger


class SampleService(AbstractService):

    def __init__(self, config: Configuration):
        super().__init__()
        self.db_name = config.POSTGRES_DB
        self.table_name = config.POSTGRES_TABLE
        self.db = None
        self.metadata = None
        self.table: Union[Table | None] = None
        self.logger = Logger.get_logger(__name__)
        self.__init_db(config=config)

    def __ensure_db(self, config: Configuration):
        default_engine = create_engine(
            f'postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@'
            f'{config.POSTGRES_URL}:{config.POSTGRES_PORT}')
        default_metadata = MetaData(default_engine)

        with default_engine.connect() as connection:
            pg_table = Table('pg_database', default_metadata, Column('datname', String))
            self.logger.info('init_db')
            exists = pg_table.select().where(pg_table.c.datname == self.db_name).execute().first()
            if not exists:
                connection.execution_options(isolation_level='AUTOCOMMIT').execute(f'create database {self.db_name}')

    def __init_db(self, config: Configuration):
        self.__ensure_db(config=config)
        self.db: Engine = create_engine(
            f'postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@'
            f'{config.POSTGRES_URL}:{config.POSTGRES_PORT}/{self.db_name}')
        self.metadata: MetaData = MetaData(self.db)
        with self.db.connect():
            self.table = Table(f'{self.table_name}', self.metadata,
                               Column('id', BigInteger, primary_key=True),
                               Column('uuid', String, nullable=False, unique=True, default=uuid.uuid4),
                               Column('message', String), Column('value', BigInteger),
                               Column('creation_ts', BigInteger,
                                      default=lambda: datetime.now().timestamp() * 1000))
            self.logger.info(f'creating table {self.table_name}')
            self.table.create(checkfirst=True)

    def create(self, any_object: Any):
        pass

    def read(self, uuids: List[str] = None):
        with self.db.connect() as connection:
            self.logger.info(f'querying sample table')
            query = self.table.select()
            results = connection.execute(query).mappings().all()
            return results

    def update(self, any_object: Any):
        pass

    def delete(self, identifier: Any):
        pass

    @staticmethod
    def get() -> SampleService:
        return SampleService(config=Configuration.get())
