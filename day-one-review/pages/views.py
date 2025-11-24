from django.shortcuts import render

def homepage(request):
    context={
        # title rating location image
        "reviews": [
            {
                "title": "Chett's Hamburger Palace",
                "rating": 5,
                "location": "International Space Station",
                "image": "https://www.nasa.gov/wp-content/uploads/2023/02/International-Space-Station-in-2021.jpg?w=1536"
            },
            {
                "title": "Arby's",
                "rating": 1,
                "location": "nah",
                "image": "https://flynn.com/wp-content/uploads/2023/10/Arbys-e1698374805908.jpg"
            },
        ]
    }
    return render(request, "pages/homepage.html", context)

def restaurant_details(request, name):
    context = {
        "restaurant_name": name
    }
    return render(request, "pages/restaurant_details.html", context)