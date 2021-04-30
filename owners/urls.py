from django.urls import path
import owners.views as ov

urlpatterns = [
    path("", ov.OwnersView.as_view()),
    path("dogs/", ov.DogsView.as_view()),
    path("create/", ov.createOwner),
    path("createDog/", ov.createDog),
]
