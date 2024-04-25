from django.shortcuts import render
from rest_framework import generics
from .models import MoleculesList
from .serializers import MoleculesListSerializer
# Create your views here.

class MoleculesListCreate(generics.ListCreateAPIView):
    queryset = MoleculesList.objects.all()
    serializer_class = MoleculesListSerializer

class MoleculesListRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoleculesList.objects.all()
    serializer_class = MoleculesListSerializer
    lookup_field = "pk" # this is the primary key, in this case the mandatory "id" field