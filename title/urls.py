from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='homepage'),
    path('idea', views.idea, name='idea'),
    path('create', views.create, name='create'),
    path('modifying', views.modifying, name='modifying'),
    path('deleting', views.deleting, name='deleting'),
]
