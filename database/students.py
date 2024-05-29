import azure.functions as func
import logging
import json
import mariadb

students = func.Blueprint()

def get_students() -> list[any]:
    try:
        con = mariadb.connect(
            host="localhost",
            user="sampleuser",
            password="samplepass",
            database="test"
        )
    except mariadb.Error as err:
        print(f'Connection failed:{err}')
        return []
    
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return students        

@students.route(route="Students", auth_level=func.AuthLevel.FUNCTION)
def Students(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Students request.')

    students = get_students()

    if len(students) > 0:
        return func.HttpResponse(json.dumps(students), 
                                 status_code=200)
    else:
        return func.HttpResponse(
             "Failded get student records",
             status_code=400
        )