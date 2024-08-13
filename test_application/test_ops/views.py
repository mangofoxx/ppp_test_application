from django.views.generic import ListView
from django.views.generic.detail import DetailView

from test_ops.models import Project, TestScenario

"""
TODO Projects should be loaded into view
"""


class ProjectListView(ListView):
    pass


projects = [
    {
        'project_name': 'Project 1',
        'project_description': 'Desc Project 1',
        'date_added': 'Avgust 10 2024'
    },
    {
        'project_name': 'Project 2',
        'project_description': 'Desc Project 2',
        'date_added': 'Avgust 10 2024'
    }
]


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
