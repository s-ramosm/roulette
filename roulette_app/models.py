from django.db import models

# Create your models here.
class Roulette(models.Model):
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Roulette {self.id}"