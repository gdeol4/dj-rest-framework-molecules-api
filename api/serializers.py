from rest_framework import serializers
from .models import MoleculesList

class MoleculesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoleculesList
        fields = ["id", "smiles", "molecular_weight"]