from django.conf.urls import url
from django.contrib import admin
from address_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', views.home),
    url(r'^agregar_usuario/', views.agregar_usuario),
    url(r'^buscar_usuario/', views.buscar_usuario),
]
