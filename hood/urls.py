from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('',views.index,name = 'index'),
    path('register/', views.register, name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/edit', views.edit_profile, name='edit'),
    path('create-mtaa/', views.create_mtaa, name='create_mtaa'),
    path('mitaa/', views.mitaa, name='mitaa'),
    path('join-mtaa/<id>', views.join_mtaa, name='join_mtaa'),
    
]