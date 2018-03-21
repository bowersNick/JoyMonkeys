from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views import generic
from .models import User, Workout

class IndexView(generic.ListView):
   template_name = "exercise/index.html"
   context_object_name = "latest_user_list"

   def get_queryset(self):
       return User.objects.filter(
           pub_date__lte=timezone.now()
           ).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    template_name = "exercise/detail.html"

    def set_workout(self, user_id):
        p = get_object_or_404(User, pk=user_id)
        # try:
        #     p.workout_set.set()


class ResultsView(generic.DetailView):
   model = User
   template_name = "exercise/results.html"

   # def vote(request, question_id):
   #     p = get_object_or_404(User, pk=question_id)
   #     try:
   #         selected_choice = p.choice_set.get(pk=request.POST['choice'])
   #     except (KeyError, Choice.DoesNotExist):
   #         return render(request, 'my_application/detail.html', {
   #             'question': p,
   #             'error_message': "You didn't select a choice",
   #         })
   #     else:
   #         selected_choice.votes += 1
   #         selected_choice.save()
   #         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
