from django.db import models

# Create your models here.

class MoleculesList(models.Model):
    smiles = models.CharField(max_length=150)
    molecular_weight = models.TextField()

    def __str__(self):
        return self.smiles