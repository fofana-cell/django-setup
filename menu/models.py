from django.db import models

class Menu(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)