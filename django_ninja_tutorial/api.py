from ninja import NinjaAPI
import orjson
from ninja.parser import Parser
from ninja.renderers import BaseRenderer

from myapp.api import router as myapp_router, InvalidToken
from events.api import router as events_router, RandomServiceError
from company.api import router as company_router


api = NinjaAPI(docs_url="docs/", csrf=True)


@api.exception_handler(InvalidToken)
def on_invalid_token(request, exc):
    return api.create_response(
        request, {"detail": "Invalid Token Supplied"}, status=401
    )


api.add_router("myapp/", myapp_router, tags=["myapp"])
api.add_router("company/", company_router, tags=["company"])


class ORJSONParser(Parser):
    def parse_body(self, request):
        return orjson.loads(request.body)


class ORJSONRenderer(BaseRenderer):
    media_type = "application/json"

    def render(self, request, data, *, response_status):
        return orjson.dumps(data)


api_v2 = NinjaAPI(
    version="2.0.0", docs_url="docs/", parser=ORJSONParser(), renderer=ORJSONRenderer()
)
api_v2.add_router("events/", events_router, tags=["events"])


@api_v2.exception_handler(RandomServiceError)
def service_unavailable(request, exc):
    print(exc)
    # return api.create_response(request, {"message": "Please Retry later."}, status=503)
