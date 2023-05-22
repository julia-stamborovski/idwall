from django.urls import path
from . import views

urlpatterns = [
    path('wanted-persons/', views.WantedPersonListView.as_view(), name='wanted-persons'),
    path('wanted-persons/<int:pk>/', views.WantedPersonDetailView.as_view(),  name='wanted-person-detail'),
]