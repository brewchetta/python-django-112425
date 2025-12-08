from django.urls import path
from . import views

urlpatterns = [
    # LOTTERY NUMBER PATHS

    path('', views.LotteryNumberListView.as_view(), name='homepage'),

    path('lotto-number/<int:pk>', views.LotteryNumberDetailView.as_view(), name="lotto_number_detail"),

    path('lotto-number/create', views.LotteryNumberCreateView.as_view(), name="lottery_number_create"),

    # WINNER PATHS

    path('winners', views.WinnerListView.as_view(), name="winners_list"),

    path('winners/<int:pk>', views.WinnerDetailView.as_view(), name="winners_detail")
]