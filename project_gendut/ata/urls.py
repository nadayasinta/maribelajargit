from django.urls import path
from . import views

urlpatterns = [
    path('mentor/input/',views.inputmentor,name='halaman_input_mentor'),

]
