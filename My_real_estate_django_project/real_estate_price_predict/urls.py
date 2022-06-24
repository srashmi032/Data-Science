from django.urls import path
from polls import views
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("predict/",views.predict,name='predict')
]