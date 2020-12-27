from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass


class PokemonType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class PokemonSpecies(models.Model):
    name = models.CharField(max_length=255)
    evolution_level = models.IntegerField(blank=True,
                                          null=True)
    show_type = models.ForeignKey(PokemonType, on_delete=models.CASCADE)
    next_evolution = models.ForeignKey('self', on_delete=models.CASCADE,
                                       blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Pokemon(models.Model):
    nickname = models.CharField(max_length=255)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    level = models.IntegerField()
    trainer = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.level >= self.species.evolution_level:
            self.species = self.species.next_evolution
        super(Pokemon, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.nickname}'


