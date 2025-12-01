from django.shortcuts import render

def home(request):
    context = {
        "video_ids": [
            "jMJ6oF-4CcY?si=QZhrRtZgZi6Js25J",
            "EPhWR4d3FJQ?si=Gup9VcEf8cm4nppy"
        ]
    }
    return render(request, 'pages/home.html', context)