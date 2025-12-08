from django.http import HttpResponse
from django.views import View # base view 


# we want the greetings view to always return a get request
class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)

# You can override that in a subclass:

# easily update it for overriding GreetingView's greeting
class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"

# The overall effect is that views' functionality can be modularized.  