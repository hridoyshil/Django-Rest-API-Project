from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes, APIView
from django.shortcuts import render

from .serializers import *
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
        serializer = Contactserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    # def put(self, request, format=None):
    #     contact = Contact.objects.get(id=1)
    #     serializer = ContactserializerOne(data=request.data, instance=contact)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data)

    def get(self, request, format=None):
        queryset = Contact.objects.get(id=1)
        serializer = Contactserializer(queryset, many=False)
        return Response(serializer.data)


from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from .models import BlogPost
from rest_framework import status


class PostCreatePIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = BlogPost.objects.all()
    serializer_class = Postserializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = PostDetailsserializer(instance=instance, many=False)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PostDetailsserializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        quaryset = BlogPost.objects.filter(is_active=False)
        return quaryset


# class POSTLISTAPIVIEW(ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = BlogPost.objects.all()
#     serializer_class = PostDetailsserializer
