from django.urls import path


from . import views

urlpatterns = [
    path("forecast", views.create, name="create"),
]