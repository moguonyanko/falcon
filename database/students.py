import azure.functions as func
import logging
import mysql.connector

students = func.Blueprint()

async def get_students():
    db = mysql.connector.connect(
        host="localhost",
        user="sampleuser",
        password="samplepass",
        database="test"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    results = cursor.fetchall()
    return results        

@students.route(route="Students", auth_level=func.AuthLevel.FUNCTION)
def Students(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Students request.')

    results = get_students()

    if len(results) > 0:
        return func.HttpResponse(students)
    else:
        return func.HttpResponse(
             "Failded get student records",
             status_code=400
        )