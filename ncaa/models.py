from django.db import models

# Create your models here.
class Conference(models.Model):
  """A conference is a collection of teams and is part of the NCAA league"""
  name = models.CharField(max_length=200)

  def __str__(self):
    """Return a string representation of the conference"""
    return self.name


class Team(models.Model):
  """A team is a collection of players and is part of a conference"""
  conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)

  class Meta:
    verbose_name_plural = 'teams'

  def __str__(self):
    """Return a string representation of the team"""
    return self.name