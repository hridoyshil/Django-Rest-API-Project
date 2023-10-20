from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, APIView
from django.shortcuts import render

from .serializers import Contactserializer, ContactForm
from .models import Contact

# Create your views here.


def homeView(request):
    return render(request, "index.html")


@api_view(["GET", "POST"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
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


from django.contrib.auth.models import User


@api_view(["POST"])
def registrationAPI(request):
    if request.method == "POST":
        username = request.data["username"]
        email = request.data["email"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        if User.objects.filter(username=username).exists():
            return Response({"error": "An user with that username already exists!"})
        if password1 != password2:
            return Response({"error": "Two password didn't matched!"})

        user = User()
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.is_active = True
        user.set_password(raw_password=password1)
        user.save()

        return Response({"Success": "User successfully Registered!"})


class ContactAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        # data= request.data
        # form= ContactForm(request.POST)
        # if form.is_valid():
        #     form.save()

        serializer = Contactserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"Success": serializer.data})

    def get(self, request, format=None):
        queryset = Contact.objects.get(id=1)
        serializer = Contactserializer(queryset, many=False)
        return Response(serializer.data)
