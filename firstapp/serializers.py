from django import forms
from .models import Contact, BlogPost
from rest_framework import serializers
from django.db import models


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class Contactserializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields = "__all__"
        fields = ["name", "email", "phone", "subject", "details"]


# class ContactserializerOne(serializers.Serializer):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#     phone = models.CharField(max_length=200)
#     subject = models.CharField(max_length=200)
#     details = models.CharField(max_length=200)

#     def create(self, validated_data):
#         return Contact(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.email = validated_data.get("email", instance.email)
#         instance.phone = validated_data.get("phone", instance.phone)
#         instance.subject = validated_data.get("subject", instance.subject)
#         instance.details = validated_data.get("details", instance.details)
#         instance.save()
#         return instance


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        # fields = "__all__"
        exclude = ["user"]


class PostDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = "__all__"
