from django.urls import path
from productsapp import views

urlpatterns=[
    path("",views.index)
]