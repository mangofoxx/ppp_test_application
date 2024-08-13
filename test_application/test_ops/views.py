from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.views.generic.detail import DetailView

from test_ops.models import Project, TestScenario


class ProjectListView(ListView):
    pass


class HomeView(ListView):
    model = Project
    template_name = 'test_ops/home.html'
    context_object_name = 'projects'

    # def get_queryset(self):
    #     return Project.objects.all() I dont need this for now, TODO add pagination


class ProjectDetailsView(DetailView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_scenarios'] = TestScenario.objects.filter(project=self.object)
        return context


class TestScenarioView(DetailView):
    model = TestScenario
    template_name = 'test_ops/test_scenario_detail.html'
    context_object_name = 'tests'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = Project.objects.filter(id=self.object.project_id).first()
        return context


class TestScenarioCreateView(LoginRequiredMixin, CreateView):
    model = TestScenario
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'pk': self.object.project_id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.project_id = self.kwargs.get('project_id')
        return super().form_valid(form)


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description']

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        """
        Check if current user is owner of the project
        :return: Boolean
        """
        project = self.get_object()

        if project.owner == self.request.user:  # Check if current user is owner
            return True

        return False


class TestScenarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TestScenario

    def get_success_url(self):
        return reverse_lazy('project-details', kwargs={'pk': self.object.project_id})

    def test_func(self):
        """
        Check if current user is owner of the project
        :return: Boolean
        """
        test_scenario = self.get_object()

        if test_scenario.owner == self.request.user:  # Check if current user is owner
            return True

        return False
