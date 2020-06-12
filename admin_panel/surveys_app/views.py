from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Survey, Pages, Question, QuestionType, Answer, MonoResponse, PolyResponse
from .forms import StepOneForm, StepTwoForm, StepThreeForm, PageForm, PageForm2, QuestionForm, AnswerForm, ResponseForm
from formtools.wizard.views import SessionWizardView


# удаление страницы - работает
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Pages
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = Pages.objects.get(id=kwargs['pk']).survey.id
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('surveys:survey', kwargs={'pk': self.survey_id})

    def delete(self, request, *args, **kwargs):
        return super(DeleteView, self).delete(request,  *args, **kwargs)


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
    model = Pages
    template_name = 'surveys_app/survey.html'
    success_url = '/'
    form_class = PageForm2

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
    model = Pages
    template_name = 'surveys_app/page.html'


class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Pages
    template_name = 'surveys_app/upd_page.html'
    fields = ('page_name', 'page_help',)
    success_url = reverse_lazy('')

    def post(self, request, *args, **kwargs):
        self.survey_id = Pages.objects.get(id=kwargs['pk']).survey.id
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


# приветствие
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


# инструкция
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


#  прощание
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
    model = Pages
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
        page = get_object_or_404(Pages, pk=self.page_pk)
        form.instance.page = page
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('surveys:page', kwargs={'pk': self.page_pk})


class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    template_name = 'surveys_app/upd_question.html'
    fields = ('question_type', 'question_text', 'question_help')
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


class SurveyWelcome(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = 'surveys_app/welcome.html'


class SurveyInstruction(LoginRequiredMixin, DetailView):
    model = Survey
    template_name = 'surveys_app/instruction.html'


class SurveyPagesListView(LoginRequiredMixin, ListView):
    model = Pages
    template_name = 'surveys_app/pages.html'
    paginate_by = 1

    # def get_queryset(self):
    #     self.survey = get_object_or_404(Survey, name=self.kwargs['survey'])
    #     return Pages.objects.filter(survey=self.survey)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ResponseForm()
        return context
