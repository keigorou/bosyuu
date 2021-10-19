from re import U
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('/', views.ThanksView.as_view(), name='thanks'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('<slug:slug>/', views.IndexView.as_view(), name='index'),
    path('<slug:slug>/<int:pk>/', views.DetailView.as_view(), name='detail'),
]