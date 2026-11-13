from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_cover, name='book_cover'),
    path('cover/', views.book_cover, name='book_cover_alias'),
]
