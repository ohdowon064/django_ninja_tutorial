from ninja import NinjaAPI

from myapp.api import router as myapp_router, InvalidToken
from events.api import router as events_router
from company.api import router as company_router


api = NinjaAPI(docs_url="docs/", csrf=True)


@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(
        request, {"detail": "Invalid Token Supplied"}, status=401
    )


api.add_router("myapp/", myapp_router, tags=["myapp"])
api.add_router("company/", company_router, tags=["company"])

api_v2 = NinjaAPI(version="2.0.0", docs_url="docs/")
api_v2.add_router("events/", events_router, tags=["events"])
