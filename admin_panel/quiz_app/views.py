from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import Question, Answer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class IndexView(ListView):
    template_name = 'quiz_app/index.html'
    context_object_name = 'latest_questions_list'

    def get_queryset(self):
        """Вернуть 2 последних вопроса"""
        return Question.objects.order_by('-date_published')[:2]


@method_decorator(csrf_exempt, name='dispatch')
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'quiz_app/detail.html'


@csrf_exempt
def vote(request, poll_id):
    question = get_object_or_404(Question, pk=poll_id)

    if request.POST.get('answer'):
        selected_answer = question.answer_set.get(pk=request.POST['answer'])
        selected_answer.votes += 1
        selected_answer.save()
        return HttpResponseRedirect(reverse('quiz:results', args=(question.id,)))
    else:
        return render(request, 'quiz_app/detail.html', {
            'question': question,
            'error_message': "Вы не выбрали ответ.",
        })


@method_decorator(csrf_exempt, name='dispatch')
class ResultsView(DetailView):
    model = Question
    template_name = 'quiz_app/results.html'
