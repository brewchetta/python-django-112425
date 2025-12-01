from django.urls import path
from . import views # do we need the "from ."

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("restaurant/<slug:name>", views.restaurant_details, name="restaurant_details")
]

# 1. build two views for the app
# 2. in one of the html pages use a for loop
# 3. in one of the views use a dictionary in your context and grab that data to show on the html page

# RETURN AT 4:40pm EST