from django.urls import path
from test_ops.views import (
    HomeView,
    ProjectDetailsView,
    TestScenarioView,
    TestScenarioCreateView,
    TestScenarioDeleteView,
    ProjectCreateView,
    ProjectDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='test_ops-home'),
    path('projects/<int:pk>', ProjectDetailsView.as_view(), name='project-details'),
    path('projects/new', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='project-delete'),
    path('projects/<int:project_id>/<int:pk>', TestScenarioView.as_view(), name='test_scenario-details'),
    path('projects/<int:project_id>/<int:pk>/delete', TestScenarioDeleteView.as_view(), name='test_scenario-delete'),
    path('projects/<int:project_id>/new/', TestScenarioCreateView.as_view(), name='test_scenario-create'),
]