from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('login/', views.user_login, name='login'),  
    path('new/', views.book_new, name='book_new'),
    path('edit/<int:pk>/', views.book_edit, name='book_edit'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.user_logout, name='logout'),
]