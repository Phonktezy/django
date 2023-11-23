from Yougene import views
from django.urls import path

urlpatterns = [
path('first/', views.index, kwargs={'name':'Yougene', 'surname': 'Batsalay', 'age': '15 years', 'hobby': 'programming'}),
path('about/', views.about, name='about', kwargs={'place': 'Belarus', 'grades': '6,5', 'like': 'yes, i like'}),
path('contacts/', views.contacts, name='about', kwargs={'git': 'phonktezy', 'tel': 'qwkdisl'}),
]
