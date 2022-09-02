from fastapi import APIRouter

from config import connection
from models import Student
from schemas import list_of_student_entity
from bson import ObjectId

student_router = APIRouter()


@student_router.get('/students')
async def find_all_students():
    return list_of_student_entity(connection.local.student.find())


@student_router.get('/students/{student_id}')
async def find_student_by_id(student_id: str):
    return list_of_student_entity(connection.local.student.find({'_id': ObjectId(student_id)}))


@student_router.post('/students')
async def create_student(student: Student):
    connection.local.student.insert_one(dict(student))
    return list_of_student_entity(connection.local.student.find())


@student_router.put('/students/{student_id}')
async def update_student(student_id: str, student: Student):
    connection.local.student.find_one_and_update(
        {'_id': ObjectId(student_id)},
        {'$set': dict(student)}
    )
    return list_of_student_entity(connection.local.student.find({'_id': ObjectId(student_id)}))


@student_router.delete('/students/{student_id}')
async def delete_student(student_id: str):
    connection.local.student.delete_one({'_id': ObjectId(student_id)})
    return list_of_student_entity(connection.local.student.find())
