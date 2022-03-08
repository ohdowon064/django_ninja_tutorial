from django.http import HttpRequest
from django.core.handlers.asgi import ASGIRequest
from ninja import NinjaAPI, Path

from myapp.schema import PathDate

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

@api.get("/items/{int:item_id}")
def read_item(request: ASGIRequest, item_id):
    return {"item_id": item_id}

@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}

weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]

@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons[offset: offset + limit]