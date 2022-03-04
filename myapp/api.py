from django.http import HttpRequest
from django.core.handlers.asgi import ASGIRequest
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/hello")
def hello(request: ASGIRequest):
    return "Hello World"


@api.api_operation(["POST", "PATCH"], "/path")
def mixed(request: ASGIRequest):
    if request.method == "POST":
        return "This is POST Path."

    elif request.method == "PATCH":
        return "This is PATCH Path."

@api.get("/items/{item_id}")
def read_item(request: ASGIRequest, item_id: int):
    return {"item_id": item_id}

