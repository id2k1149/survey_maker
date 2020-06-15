from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Survey, Page, Question, Answer, Response
from .forms import StepOneForm, StepTwoForm, StepThreeForm, ContactForm
from .forms import PageForm, QuestionForm, AnswerForm, ResponseFormDemo, ResponseForm, SurveyCode
from formtools.wizard.views import SessionWizardView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


def main_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']
            # last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                'Contact message',
                f'Ваш сообщение "{message}" принято',
                'id2k1149@gmail.com',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('surveys:index'))
        else:
            return render(request, 'surveys_app/index.html', context={'form': form})
    else:
        form = ContactForm()
        return render(request, 'surveys_app/index.html', context={'form': form})


# удаление страницы - работает
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = Page.objects.get(id=kwargs['pk']).survey.id
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})

    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request,  *args, **kwargs)


# удаление вопроса - работает
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.page_id = Question.objects.get(id=kwargs['pk']).page.id
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:page', kwargs={'pk': self.page_id})

    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request,  *args, **kwargs)


# удаление опроса - работает
class SurveyDeleteView(LoginRequiredMixin, DeleteView):
    model = Survey
    success_url = reverse_lazy('surveys:surveys')

    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request,  *args, **kwargs)


# ListView - все опросы - работает
class SurveysListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'surveys_app/surveys.html'


# FormWizardView - добавление по шагам опроса - работает
class FormWizardView(LoginRequiredMixin, SessionWizardView):
    template_name = "surveys_app/add_survey.html"
    form_list = [StepOneForm, StepTwoForm, StepThreeForm]

    def done(self, form_list, **kwargs):
        data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        Survey.objects.create(**data)
        # если нужна страница Завершения
        # return render(self.request, 'surveys_app/done.html', {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
        return HttpResponseRedirect(reverse("surveys:surveys"))


# SurveyDetailView - отдельный опрос - работает
class SurveyDetailView(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = 'surveys_app/survey.html'


# добавление пустой страницы - работает
class AddPageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'surveys_app/survey.html'
    success_url = '/'
    form_class = PageForm

    def post(self, request, *args, **kwargs):
        self.survey_pk = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        survey = get_object_or_404(Survey, pk=self.survey_pk)
        form.instance.survey = survey
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_pk})


class PageDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'surveys_app/page.html'


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'surveys_app/upd_page.html'
    fields = ('page_name', 'page_help',)
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = Page.objects.get(id=kwargs['pk']).survey.id
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


# редактирование страницы шаг 1
# class SurveyUpdatePageView(LoginRequiredMixin, DetailView):
#     model = Survey
#     template_name = 'surveys_app/edit_page.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = PageForm
    #     return context


# редактирование страницы шаг 2
# class SurveyUpdatePageUpdateView(LoginRequiredMixin, UpdateView):
#     model = Pages
#     template_name = 'surveys_app/edit_page.html'
#     success_url = '/'
#
#     def post(self, request, *args, **kwargs):
#         self.survey_pk = kwargs['pk']
#         return super().post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     survey = get_object_or_404(Survey, pk=self.survey_pk)
    #     form.instance.survey = survey
    #     return super().form_valid(form)

    # def get_success_url(self):
    #     return reverse('surveys:survey', kwargs={'pk': self.survey_pk})


# страница приветствие
class HelloUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['hello_title', 'hello_text', ]
    template_name = 'surveys_app/hello.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


# страница инструкция
class InfoUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['info_title', 'info_text', ]
    template_name = 'surveys_app/info.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


#  страница прощание
class ByeUpdateView(LoginRequiredMixin,  UpdateView):
    model = Survey
    fields = ['bye_title', 'bye_text', ]
    template_name = 'surveys_app/bye.html'
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = kwargs['pk']
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})


class PageQuestionDetailView(LoginRequiredMixin, DetailView):
    model = Page
    template_name = 'surveys_app/add_question.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = QuestionForm()
        return context


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    template_name = 'surveys_app/add_question2.html'
    success_url = reverse_lazy('/')
    form_class = QuestionForm

    def post(self, request, *args, **kwargs):
        self.page_pk = kwargs['pk']
        print(self.page_pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        page = get_object_or_404(Page, pk=self.page_pk)
        form.instance.page = page
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:page', kwargs={'pk': self.page_pk})


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'surveys_app/upd_question.html'
    fields = ('question_type', 'question_title', 'question_help')
    success_url = reverse_lazy('/')

    def post(self, request, *args, **kwargs):
        self.page_id = Question.objects.get(id=kwargs['pk']).page.id
        print(self.page_id)
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:page', kwargs={'pk': self.page_id})


class QuestionAnswerDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'surveys_app/add_answer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AnswerForm()
        return context


class QuestionAnswerCreateView(LoginRequiredMixin, CreateView):
    model = Answer
    template_name = 'surveys_app/add_answer2.html'
    success_url = reverse_lazy('/')
    form_class = AnswerForm

    def post(self, request, *args, **kwargs):
        self.question_pk = kwargs['pk']
        print("self.question_pk = ", self.question_pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.question_pk)
        form.instance.question = question
        print("question = ", question)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:add_answer', kwargs={'pk': self.question_pk})


class SurveyWelcome(DetailView):
    model = Survey
    template_name = 'surveys_app/welcome.html'


# шаг 1 (хотел сохранить рандом-код)
class SurveyInstruction(DetailView):
    model = Survey
    template_name = 'surveys_app/instruction.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SurveyCode()
        return context


# шаг 2 (хотел сохранить рандом-код)
class StartSurveyCreateView(CreateView):
    model = Response
    template_name = 'surveys_app/pages_d3.html'
    success_url = reverse_lazy('')
    form_class = SurveyCode

    def post(self, request, *args, **kwargs):
        self.page_pk = kwargs['pk']
        print("self.page_pk from instruction page = ", self.page_pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        page = get_object_or_404(Page, pk=self.page_pk)
        survey = get_object_or_404(Survey, pk=page.survey.id)
        form.instance.survey = survey
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:pages_d', kwargs={'pk': self.page_pk})


class SurveySeeYouLater(DetailView):
    model = Survey
    template_name = 'surveys_app/see_you_later.html'


# демо
class SurveyPagesListViewDemo(ListView):
    model = Page
    template_name = 'surveys_app/pages.html'
    paginate_by = 1

    def get_queryset(self):
        return super().get_queryset().filter(survey_id=self.kwargs['survey_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseFormDemo()
        return context


# не используется
def create_respond(request):
    if request.method == 'POST':
        form = ResponseFormDemo(request.POST)
        if form.is_valid():

            # survey = form.cleaned_data['survey']
            # question = form.cleaned_data['question']
            # answer = form.cleaned_data['answer']
            # MonoResponse.objects.create(survey=survey, question=question, answer=answer)
            form.save()
            return HttpResponseRedirect(reverse('surveys:surveys'))
        else:
            return render(request, 'surveys_app/create.html', context={'form': form})
    else:
        form = ResponseFormDemo()
        return render(request, 'surveys_app/create.html', context={'form': form})


# не используется
class SurveyResponsesCreateView(CreateView):
    fields = ('answer',)
    model = Response
    success_url = reverse_lazy('surveys:see_you_later')
    template_name = 'surveys_app/create2.html'

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super().form_valid(form)


# для пятницы шаг 1
class PageResponseDetailView(DetailView):
    model = Page
    template_name = 'surveys_app/pages_d.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseForm()
        return context


# для пятницы шаг 2
class ResponseCreateView(CreateView):
    model = Response
    template_name = 'surveys_app/pages_d2.html'
    success_url = reverse_lazy('/')
    form_class = ResponseForm

    def post(self, request, *args, **kwargs):
        self.question_pk = kwargs['pk']
        print("self.question_pk from last page = ", self.question_pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.question_pk)
        print("question= ", question, "page_pk= ", question.page.id)
        form.instance.question = question
        page = get_object_or_404(Page, pk=question.page.id)
        print("page = ", page)
        survey = get_object_or_404(Survey, pk=page.survey.id)
        form.instance.survey = survey
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:pages_d', kwargs={'pk': self.question_pk})


# демо 2 шаг1
class SurveyQuestionsListView(ListView):
    model = Question
    template_name = 'surveys_app/questions.html'
    paginate_by = 1

    def get_queryset(self):
        survey_id = self.kwargs['survey_id']
        qs = super().get_queryset()
        questions = qs.filter(page__survey=survey_id)
        return questions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseForm()
        return context


# # для  шаг 2
@method_decorator(csrf_exempt, name='dispatch')
class ResponseCreateView2(CreateView):
    model = Response
    template_name = 'surveys_app/pages_d2.html'
    success_url = reverse_lazy('/')
    form_class = ResponseForm

    def post(self, request, *args, **kwargs):
        self.question_pk = kwargs['pk']
        print("self.question_pk from last page = ", self.question_pk)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        question = get_object_or_404(Question, pk=self.question_pk)
        print("question= ", question, "page_pk= ", question.page.id)
        form.instance.question = question
        page = get_object_or_404(Page, pk=question.page.id)
        print("page = ", page)
        survey = get_object_or_404(Survey, pk=page.survey.id)
        form.instance.survey = survey
        return super().form_valid(form)

    def get_success_url(self):
        question = get_object_or_404(Question, pk=self.question_pk)
        page = get_object_or_404(Page, pk=question.page.id)
        survey = get_object_or_404(Survey, pk=page.survey.id)
        return reverse('surveys:see_you_later', kwargs={'pk': survey.id})


