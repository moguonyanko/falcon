'''
参考:
https://github.com/Azure/azure-functions-python-extensions/blob/main/azure-functions-extension-fastapi/samples/fastapi_samples_streaming_download/function_app.py
'''
import time
import logging
import azure.functions as func
from azure.functions.extension.fastapi import Request, StreamingResponse

streaming_download = func.Blueprint()

"""
サンプルデータを生成
"""
def generate_sensor_data():
    for i in range(10):
        temperature = 20 + i
        humidity = 50 + i
        yield f"data: {{'temperature': {temperature}, 'humidity': {humidity}}}\n\n"
        time.sleep(1)

@streaming_download.route(route="streaming_download", auth_level=func.AuthLevel.FUNCTION)
def streaming_download(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('streaming_download request.')
    return StreamingResponse(generate_sensor_data(), media_type='text/event-stream')
