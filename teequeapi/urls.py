from django.urls import path
from . import views

urlpatterns = [
    path('bye/', views.bye, name='bye'),

]
