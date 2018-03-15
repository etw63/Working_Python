from django.urls import path

from . import views

app_name = 'tubes'

urlpatterns = [
    path('',views.evprint, name='evprint'),
]