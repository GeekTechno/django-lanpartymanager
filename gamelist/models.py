from django.core.urlresolvers import reverse
from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=120)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game:list')


class Connection(models.Model):
    game = models.ForeignKey(Game)
    details = models.CharField(max_length=255)

    def __unicode__(self):
        return '[' + self.game.name + '] ' + self.details[:30]

    def get_absolute_url(self):
        return reverse('game:list')