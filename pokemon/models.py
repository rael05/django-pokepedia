from django.db import models

class Movement(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=50)
    power = models.IntegerField()
    accuracy = models.IntegerField()
    points = models.IntegerField()
    special = models.BooleanField()

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    fields_to_display = [
        "number",
        "name",
        "img",
        "health",
        "physical_attack",
        "physical_defence",
        "speed",
        "special_attack",
        "special_defence"
    ]

    number = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')

    health = models.IntegerField()
    physical_attack = models.IntegerField()
    physical_defence = models.IntegerField()
    speed = models.IntegerField()
    special_attack = models.IntegerField()
    special_defence = models.IntegerField()

    gen1_special = models.IntegerField(blank=True)
    movement = models.ManyToManyField(Movement, through='Perlevel')

    def __str__(self):
        return self.name
    
    @classmethod
    def display_properties(cls):
        return list(cls.objects.values(*cls.fields_to_display))
    
class Perlevel(models.Model):
    movement = models.ForeignKey(Movement, on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    level = models.IntegerField()