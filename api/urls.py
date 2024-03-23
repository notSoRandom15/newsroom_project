from django.urls import path
from ninja import NinjaAPI
from .articles import articles_router
from .blocks import blocks_router

app_name = 'api'

api = NinjaAPI()

api.add_router("articles/", articles_router, tags=["articles"])
api.add_router("blocks/", blocks_router)

urlpatterns = [
    path('', api.urls),
]