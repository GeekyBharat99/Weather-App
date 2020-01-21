# this is my views.py file
from django.shortcuts import render

def Home(request):
    import json
    import requests

    if request.method == "POST":
        City_Name = request.POST["City_Name"]
        api_requests = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + City_Name + "&units=metric&APPID=bf17de17116094a98f18a1c9199596e8")
        api_requests1 = requests.get(
            "https://api.waqi.info/feed/" + City_Name + "/?token=75872b25be4acc88ca239f901753f1f7df3da5e3")
        try:
            api = json.loads(api_requests.content)
            api1 = json.loads(api_requests1.content)
        except Exception as e:
            api = "Error..."
            api1 = "Error..."
        return render(request, "index.html", {'api': api, 'api1': api1})

    else:
        api_requests = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=bhopal&units=metric&APPID=bf17de17116094a98f18a1c9199596e8")
        api_requests1 = requests.get(
            "https://api.waqi.info/feed/bhopal/?token=75872b25be4acc88ca239f901753f1f7df3da5e3")
        try:
            api = json.loads(api_requests.content)
            api1 = json.loads(api_requests1.content)
        except Exception as e:
            api = "Error..."
            api1 = "Error..."
        return render(request, "index.html", {'api': api, 'api1': api1})




def About(request):
    return render(request,"about.html")