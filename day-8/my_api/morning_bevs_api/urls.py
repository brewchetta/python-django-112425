from django.urls import path
from . import views

urlpatterns = [
    # BEVERAGE PATHS

    path('api/v1/beverages', views.beverages_list, name="beverages_list"),

    path('api/v1/beverages/<int:pk>', views.beverage_detail, name="beverage_detail"),

    # BRAND PATHS

    path('api/v1/brands', views.brand_list, name="brand_list"),

    path('api/v1/brands/<int:pk>', views.brand_detail, name="brand_detail")
]