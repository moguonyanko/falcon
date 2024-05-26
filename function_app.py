import azure.functions as func
import logging

from database.students import students
 
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(students)

@app.route(route="HelloWorld")
def HelloWorld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('HelloWorld request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"こんにちは, {name}。関数アプリ呼び出しは成功しました！")
    else:
        return func.HttpResponse(
             "関数アプリ呼び出し失敗",
             status_code=400
        )