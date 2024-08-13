from django.urls import path
from test_ops.views import HomeView, ProjectDetailsView, TestScenarioView

urlpatterns = [
    path('', HomeView.as_view(), name='test_ops-home'),
    path('projects/<int:pk>', ProjectDetailsView.as_view(), name='project-details'),
    path('projects/<int:fk>/<int:pk>', TestScenarioView.as_view(), name='test_scenario-details'),
]