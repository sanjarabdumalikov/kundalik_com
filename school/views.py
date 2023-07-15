from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import SchoolModel
from .serializer import SchoolSerializer

class AllCreateSchoolView(generics.ListCreateAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer


class DetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SchoolModel.objects.all()
    serializer_class = SchoolSerializer

# Create your views here.
