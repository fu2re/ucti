from django.urls import path

from ucti.views import index_view, redirect_view, infinite_view

urlpatterns = [
    path('', index_view, name='index'),
    path('<int:depth>/', redirect_view, name='multiple'),
    path('inf/', infinite_view, name='infinite'),
]
