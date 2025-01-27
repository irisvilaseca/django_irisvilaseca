from django.db import models

class Alumne(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    moduls_matriculats = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.cognom1} {self.cognom2}"

class Professor(models.Model):
    nom = models.CharField(max_length=100)
    cognom1 = models.CharField(max_length=100)
    cognom2 = models.CharField(max_length=100, blank=True, null=True)
    correu = models.EmailField()
    curs = models.CharField(max_length=50)
    tutor = models.BooleanField(default=False)
    moduls_imparteix = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.cognom1} {self.cognom2}"
