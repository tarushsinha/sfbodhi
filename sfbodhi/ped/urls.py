from django.urls import path
from . import views

urlpatterns = [
    path('persona/', views.persona_view, name='persona'),
    path('designate_rishta/', views.designate_rishta_view, name='designate_rishta'),
    path("graph/", views.relationship_graph_view, name="relationship_graph"),
]