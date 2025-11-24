from django.urls import path
from . import views # get views from the views file once they exist

urlpatterns = [
    # path('<name>/', views.<name>, name="<name>")
    path('', views.home, name="home"), # this matches the view function in views.py
    path('skills/', views.skills, name="skills"),
    path('volunteer-work/', views.volunteer_work, name="volunteer_work")
    # url path, name of the function in views, name of the view
]