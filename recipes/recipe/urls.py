from django.conf.urls.defaults import *
from recipe.models import Recipe, Ingredients

info_dict = {
    'queryset': Recipe.objects.all(),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', info_dict, name="list"),
	url(r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict, name="detail"),
	url(r'^(?P<object_id>\d+)/results/$', 'django.views.generic.list_detail.object_detail', dict(info_dict, template_name='pages/results.html'), name='results'),
	url(r'^(?P<recipe_id>\d+)/vote/$', 'recipe.views.vote', name="vote"),
)
