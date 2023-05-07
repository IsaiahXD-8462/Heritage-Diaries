from django.urls import path, include
from diary import views

urlpatterns = [
    path('all/', views.logged_in_user),
]
