from django.urls import path,include
from .import views

urlpatterns = [
path('login',views.logfn,name='login')
]
