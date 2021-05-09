from django.contrib import admin
from django.urls import path
from app.views import home, cadastrados, form

urlpatterns = [
    path("admin/", admin.site.urls),
    path("cadastrados/", cadastrados, name="cadastrados"),
    path("form/", form, name="form"),
    path("", home, name="home"),
]
