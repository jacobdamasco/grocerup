from django.db import models

# Create your models here.
PLACES = (
    ('Fridge', 'Fridge'),
    ('Freezer', 'Freezer'),
    ('Pantry', 'Pantry'),
)

class Item(models.Model):
    qty = models.IntegerField()
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=30, choices=PLACES)

    def __str__(self):
        return self.name
