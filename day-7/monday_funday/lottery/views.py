from django.shortcuts import render, redirect
from .models import LottoNumber, Winner
from django.views.generic import DetailView, ListView, CreateView
from django.urls import reverse_lazy
from .forms import WinnerForm


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


# yes you can mix class views with functional views!
def new_winner(request):
    if request.method == "GET":
        # if we have a GET request etc.
        context = { "form": WinnerForm() }
        return render(request, 'lottery/winner_form.html', context)
    elif request.method == "POST":
        # if someone is submitting with a POST
        # very importantly we need to also accept the request.FILES to get the image here
        form = WinnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('winners_list')



# below is considered the functional way of building a view
# functional ->>> it uses a function
# def homepage(request):
#     context = {
#         "lotto_numbers": LottoNumber.object.all()
#     }
#     return render(request, 'lottery/homepage.html', context)