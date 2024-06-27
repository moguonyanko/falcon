import azure.functions as func
import logging

from database.students import students
#from streaming.streaming_download import streaming_download 
from gis.area import area

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)
app.register_functions(students)
#app.register_functions(streaming_download)
app.register_functions(area)

@app.route(route="helloworld")
def HelloWorld(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('helloworld request')

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