from ninja import NinjaAPI
from myapp.api import router as myapp_router
from events.api import router as events_router

api = NinjaAPI(docs_url="/docs/")

api.add_router("/events/", events_router)
api.add_router("/myapp/", myapp_router)