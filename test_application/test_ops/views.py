from django.shortcuts import render
from django.views.generic import ListView

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


def home(request):
    context = {
        'projects': projects
    }
    return render(request, 'test_ops/home.html', context=context)
