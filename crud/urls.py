from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path("detalle/<name>/", views.vista_detalle, name='detalleCarta'),
]