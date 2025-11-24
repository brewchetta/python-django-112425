from django.shortcuts import render

def home(request):
    context = {
        "dev_name": "Chett",
        "projects": [ 
            { 
                "name": "Dad Joke Recommender",
                "link": "https://dad-joke-recommender.com"
            }, 
            {
                "name": "Dad Simulator",
                "link": "https://dad-simulator.com"
            },
            {
                "name": "Cat Dad Adoption Agency",
                "link": "https://cat-dad-adoption-agency.gov"
            }
        ],
        "profile": {
            "username": "booger123",
            "password": "eater"
        }
    }
    return render(request, 'homepage/home.html', context)


def skills(request):
    context = {
        "tech_stack": "Python, Django, SQL, JavaScript"
    }
    return render(request, 'homepage/skills.html', context)

def volunteer_work(request):
    context = {
        "Title": "Return at 2:55pm EST"
    }
    return render(request, 'homepage/volunteer_work.html', context)