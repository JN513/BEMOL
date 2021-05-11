from django.contrib import admin
from django.urls import path
from app.views import home, cadastrados, form, delete_person

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cadastrados/", cadastrados, name="cadastrados"),
    path("form/", form, name="form"),
    path("deletar/<int:id>/", delete_person, name="deletar"),
    path("", home, name="home"),
]
