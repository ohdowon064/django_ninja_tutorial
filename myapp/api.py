from datetime import date
from typing import Optional, List

from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.core.handlers.asgi import ASGIRequest
from ninja import NinjaAPI, Path, Query, Body, Form, UploadedFile, File

from myapp.models import Task, Picture
from myapp.schema import PathDate, Filters, Item, UserIn, UserOut, TaskSchema, PictureSchema

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


@api.post("/items-blank-default")
def update2(request, item: Item = Form(...)):
    return item.dict()


@api.post("/upload")
def upload(request, file: UploadedFile = File(...)):
    data = file.read()
    print(type(data))
    print(data.__dir__())
    return {"name": file.name, "len": len(data)}


@api.post("/upload-many")
def upload_many(request, files: List[UploadedFile] = File(...)):
    return [f.name for f in files]


@api.post("/users/", response=UserOut)
def create_user(request, user_info: UserIn = Body(...)):
    user = User(username=user_info.username)
    user.set_password(user_info.password)
    user.save()
    return user


@api.get("/tasks", response=List[TaskSchema])
def tasks(request):
    return Task.objects.select_related("owner")

@api.post("/pictures", response=PictureSchema)
def create_picture(request, title: str = Body(...), image: UploadedFile = File(...)):
    return Picture.objects.create(title=title, image=image)


