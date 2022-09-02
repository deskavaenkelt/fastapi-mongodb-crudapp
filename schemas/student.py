def student_entity(db_item) -> dict:
    return {
        'id': str(db_item['_id']),
        'name': db_item['name'],
        'age': db_item['age'],
        'email': db_item['email']
    }


def list_of_student_entity(db_items) -> list:
    return [student_entity(db_item) for db_item in db_items]
