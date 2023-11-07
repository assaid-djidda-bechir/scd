from django.db import models


class Client(models.Model):
    
    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    email  = models.EmailField()
    ville  = models.CharField(max_length=30)
    code_postal  = models.CharField(max_length=30)
    telephone  = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    quantite = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nom


class Comment(models.Model):
    nom = models.CharField(max_length=200)
    email  = models.EmailField() 
    avis = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.nom