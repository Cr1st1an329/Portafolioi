from django.urls import path
from . import views 

urlpatterns = [
    path("contact/", views.contacto, name="Contacto"),

]