import random

from ninja import Router
from uuid import uuid4

from ninja.errors import HttpError

router = Router()

events = [{"id": i, "detail": uuid4().hex} for i in range(20)]
for event in events:
    event["title"] = event["detail"][:6]


@router.get("/")
def list_events(request):
    return [{"id": e["id"], "title": e["title"]} for e in events]


@router.get("{int:event_id}/")
def event_details(request, event_id: int):
    try:
        this_event = events[event_id]
    except IndexError:
        return 401, {"msg": f"{event_id} doesn't exist."}
    return {"title": this_event["title"], "detail": this_event["detail"]}


class RandomServiceError(Exception):
    pass


@router.get("/service")
def some_operation(request):
    if random.choice([True, False]):
        raise HttpError(status_code=503, message="Please retry later.")
    return {"message": "Success! You're Lucky!"}
