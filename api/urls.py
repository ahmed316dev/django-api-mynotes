from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.notes, name="notes"),
    path('notes/<str:pk>/', views.note, name="note"),
]