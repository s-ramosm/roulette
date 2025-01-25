from django.db import models

# Create your models here.
class Roulette(models.Model):

    CLOSE = "Close"
    OPEN = "Open"

    STATE_CHOICES = [
        (OPEN, 'Open'),
        (CLOSE, 'Close'),
    ]


    state = models.CharField(
        max_length=5,
        choices=STATE_CHOICES,
        default='Closed',
    )
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Roulette {self.id}"