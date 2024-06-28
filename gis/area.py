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

@area.route(route="area", auth_level=func.AuthLevel.FUNCTION)
def get_area(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('area request')

    points = [(10, 20), (20, 40), (30, 30), (40, 10), (30, 0), (20, 10)]
    polygon = Polygon(points)
    response = f'{{"area": {polygon.area}}}'

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    return func.HttpResponse(response,
                             headers={
                                 "Content-Type": "application/json"
                             })
