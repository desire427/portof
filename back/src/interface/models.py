from django.db import models


class Portofolio(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.nom
