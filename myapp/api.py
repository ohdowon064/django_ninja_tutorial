from datetime import date
from typing import Optional

from django.http import HttpRequest, HttpResponse
from django.core.handlers.asgi import ASGIRequest
from ninja import NinjaAPI, Path, Query, Body, Form

from myapp.schema import PathDate, Filters, Item

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
def read_item(request: ASGIRequest, item_id: int):
    return {"item_id": item_id}


@api.get("/events/{year}/{month}/{day}")
def events(request, date: PathDate = Path(...)):
    return {"date": date.value()}


weapons = ["Ninjato", "Shuriken", "Katana", "Kama", "Kunai", "Naginata", "Yari"]


@api.get("/weapons")
def list_weapons(request, limit: int = 10, offset: int = 0):
    return weapons[offset: offset + limit]


@api.get("/weapons/search")
def search_weapons(request, q: str, offset: int = 0):
    results = [w for w in weapons if q in w.lower()]
    print(q, results)
    return results[offset: offset + 10]


@api.get("/example")
def example(request, filters: Filters = Query(...)):
    return {"filters": filters.dict()}


@api.post("/items")
def create(request, item: Item = Body(...)):
    print("created item record in db")
    return item


@api.put("/items/{int:item_id}")
def update(
    request,
    item_id: int = Path(...),
    item: Item = Body(...)
):
    return {"item_id": item_id, "item": item.dict()}

@api.patch("/items/{int:item_id}")
def partial_update(
        request,
        item_id: int = Path(...),
        q: str = Query(...),
        item: Item = Body(...)
):
    return {"item_id": item_id, "q": q, "item": item}

@api.post("/login")
def login(
        request,
        item: Item = Form(...)
):
    return item.dict()