from recipe.models import Recipe
from recipe.models import Ingredients
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
  model = Ingredients
  extra = 3

class RecipeAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,                 {'fields': ['recipe']}),
    ('Date information',   {'fields': ['pub_date'], 'classes': ['collapse']}),
  ]
  inlines = [ChoiceInline]
  list_display = ('recipe', 'pub_date', 'was_published_today')
  list_filter = ['pub_date']
  search_fields = ['recipe']
    
admin.site.register(Recipe, RecipeAdmin)