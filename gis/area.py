# Register this blueprint by adding the following line of code
# to your entry point file.
# app.register_functions(area)
#
# Please refer to https://aka.ms/azure-functions-python-blueprints

import logging
import json
import azure.functions as func
from shapely.geometry import Polygon

area = func.Blueprint()

@area.route(route="calcarea", auth_level=func.AuthLevel.FUNCTION)
def get_area(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('area request')

    try:
        req_body = req.get_json()
        coordinates = req_body['coordinates']
        polygon = Polygon(coordinates[0])
        response = f'{{"area": {polygon.area}}}'
    except ValueError as e:
        print(e)

    return func.HttpResponse(response,
                             headers={
                                 "Content-Type": "application/json"
                             })
