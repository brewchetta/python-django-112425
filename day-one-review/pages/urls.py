from django.urls import path
from . import views # do we need the "from ."

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("restaurant/<slug:name>", views.restaurant_details, name="restaurant_details")
]