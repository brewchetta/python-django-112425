from django.shortcuts import render
from .models import LottoNumber, Winner
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy


# list view is for all items
class LotteryNumberListView(ListView):
    model = LottoNumber # this is what the object_list will be made of
    template_name = 'lottery/homepage.html'
    # this is the template we will render


# detail view is for one item
class LotteryNumberDetailView(DetailView):
    model = LottoNumber
    template_name = 'lottery/lotto_number_detail.html'


# create view is to have a form for a new item
class LotteryNumberCreateView(CreateView):
    model = LottoNumber
    fields = ['winning_numbers', 'date', 'location', 'dollar_amount', 'rounds_not_won', 'winner']
    # success_url is where we go when successful
    success_url = reverse_lazy('homepage')


# list view for all winners
class WinnerListView(ListView):
    model = Winner
    template_name = 'lottery/winner_list_view.html'


# individual view for winner
class WinnerDetailView(DetailView):
    model = Winner
    template_name = 'lottery/winner_detail_view.html'


# below is considered the functional way of building a view
# functional ->>> it uses a function
# def homepage(request):
#     context = {
#         "lotto_numbers": LottoNumber.object.all()
#     }
#     return render(request, 'lottery/homepage.html', context)