from django.shortcuts import render
from rest_framework import viewsets, permissions
from samapp.models import *
from samapp.serializers import StudentSerializer, LanguageSerializer


class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = permissions.IsAuthenticatedOrReadOnly,
