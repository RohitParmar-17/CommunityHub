from django.urls import path
from . import views

urlpatterns = [
    path('', views.topic_list_view, name='topic_list'),
    path('<int:pk>/', views.topic_detail_view, name='topic_detail'),
]
