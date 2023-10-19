from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from db import get_async_session
from operations.models import operation, ResponseModel
from operations.schemas import OperationCreate


router = APIRouter(
    prefix='/operations',
    tags=['Operation'],
)


@router.get('/', response_model=ResponseModel)
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "OK",
            "data": result.all(),
            "detail": None,
        }
    except Exception:
        return {
            "status": "ERROR",
            "data": None,
            "detail": None,
        }


@router.get('/all', response_model=ResponseModel)
async def get_all_operations(session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation)
        result = await session.execute(query)
        return {
            "status": "OK",
            "data": result.all(),
            "detail": None,
        }
    except Exception:
        return {
            "status": "ERROR",
            "data": None,
            "detail": None,
        }


@router.post('/', response_model=ResponseModel)
async def add_specific_operation(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        statement = insert(operation).values(**new_operation.dict())
        await session.execute(statement)
        await session.commit()
        return {
            "status": "OK",
            "data": None,
            "detail": None,
        }
    except Exception:
        return {
            "status": "ERROR",
            "data": None,
            "detail": None
        }