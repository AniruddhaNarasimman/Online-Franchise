from django.urls import path, include
from . import views


app_name = 'candidatereg'
urlpatterns = [
    path('',views.register, name="register")

]
