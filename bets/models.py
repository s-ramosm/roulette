from django.db import models
from roulette_app.models import Roulette
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator




# Create your models here.
class Bet(models.Model):

    RED = 'Red'
    BLACK = 'Black'
    
    COLOR_CHOICES = [
        (RED, 'Red'),
        (BLACK, 'Black'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bets')
    roulette = models.ForeignKey(Roulette, on_delete=models.CASCADE, related_name='bets')
    amount = models.FloatField(validators=[MaxValueValidator(10000), MinValueValidator(1)])
    winning_amount = models.FloatField(null=True, blank=True)
    number = models.IntegerField(validators=[MaxValueValidator(36), MinValueValidator(0)] , null=True, blank=True) 
    color = models.CharField(
        max_length=5,
        choices=COLOR_CHOICES, 
        )  
    

    def set_win_state(self, number):
        
        if number % 2 == 0 : 
            color = "Red"
        else:
            color =  "Black"

        
        print(self.number, self.number == None)
        if number == self.number: 
            self.winning_amount = self.amount * 5
        
        elif self.number == None and self.color == color:
            self.winning_amount = self.amount * 1.8

        self.save()


    def __str__(self):
        return f"Bet by {self.user.name} on Roulette {self.roulette.id}"