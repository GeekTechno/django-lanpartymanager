from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Instruction(models.Model):
    details = models.CharField(max_length=255)
    game = models.ForeignKey(Game)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '[' + self.game.name + '] ' + str(self.created_at) + self.details

    class Meta:
        ordering = ['-created_at']