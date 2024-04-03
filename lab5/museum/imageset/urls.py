from django.urls import path

from . import views

app_name = 'imageset'

urlpatterns = [
    path("", views.imageset_render, name='imageset_render'),
    path("image/<int:pk>", views.image_render, name='image_render'),
    path("delete/<int:pk>", views.delete_rectangle, name="delete_rectangle"),
]
