from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from recipe.models import Recipe, Ingredients

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
	selected_ingredients = p.ingredients_set.get(pk=request.POST['ingredients'])
  except (KeyError, Ingredients.DoesNotExist):
	return render_to_response('recipes_detail.html', {
		'recipe': p,
		'error_message': "You didn't select a choice.",
		}, context_instance=RequestContext(request))
  else:
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('recipes:results', args=(p.id,)))