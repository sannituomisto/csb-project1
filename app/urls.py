from django.urls import path
from .views import homeView, signUpView, addView, deleteView

urlpatterns = [
    path('', homeView, name='home'),
    path('signup/', signUpView, name='signup'),
    path('add/', addView, name='add'),
    path('delete/<int:taskid>', deleteView, name='delete')
]