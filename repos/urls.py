from django.urls import path

from repos import views

urlpatterns = [
    path('', views.repo_list, name='index'),
]
