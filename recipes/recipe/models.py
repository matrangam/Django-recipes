from django.db import models
import datetime
  
class Recipe(models.Model):                            
  recipe = models.CharField(max_length=200)        
  pub_date = models.DateTimeField('date created') 

  def __unicode__(self):
    return self.recipe
  
  def was_published_today(self):
    return self.pub_date.date() == datetime.date.today()
  was_published_today.short_description = 'Created today?'

class Ingredients(models.Model):
  recipe = models.ForeignKey(Recipe)
  ingredients = models.CharField(max_length=200)
  votes = models.IntegerField()
  
  def __unicode__(self):
    return self.ingredients

