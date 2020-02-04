from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('signin/', views.signin, name='signin')
]