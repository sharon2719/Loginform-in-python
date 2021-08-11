from .views import register_request
from django.urls import path
from . import views

app_name="fair_site"

urlpatterns=[
    path("",views.register_request,name="fair_site"),
    path("register/",register_request,name="register_request")
    
]
