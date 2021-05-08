from django.contrib import admin
from django.urls import path
from app.views import home, cadastrados, form, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cadastrados/', cadastrados, name='cadastrados'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('', home, name='home'),
]
