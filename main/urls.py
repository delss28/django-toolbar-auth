from django.urls import path
from main import views

urlpatterns = [
    path("", views.index, name="home"),
    path("catalog", views.catalog, name="catalog"),
    path("contact", views.contact, name="contact"),
]
