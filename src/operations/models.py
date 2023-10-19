from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, MetaData
from pydantic import BaseModel
from enum import StrEnum
from typing import Any, Optional

from operations.schemas import OperationCreate

metadata = MetaData()

operation = Table(
    'operation',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('quantity', String),
    Column('figi', String),
    Column('instrument_type', String, nullable=False),
    Column('date', TIMESTAMP),
    Column('type', String),
)


class ResponseModel(BaseModel):
    status: str
    data: None | list[OperationCreate]
    detail: None | str
