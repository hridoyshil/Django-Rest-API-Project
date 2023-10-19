from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.


def homeView(request):
    return render(request, "index.html")


@api_view(["GET", "POST"])
def firstAPI(request):
    if request.method == "POST":
        name = request.data["name"]
        age = request.data["age"]
        print(name, age)
        return Response({"name": name, "age": age})
    context = {
        "name": "Hridoy Kumar shil",
        "University": "FCI",
        "Dep": "TCT",
    }
    return Response(context)
