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
    path('mtaa/<mtaa_id>', views.mtaa, name='mtaa'),
    path('join-mtaa/<id>', views.join_mtaa, name='join_mtaa'),
    path('leave-mtaa/<id>', views.leave_mtaa, name='leave_mtaa'),
    path('occupants/<mtaa_id>', views.mtaa_occupants, name='occupants'),
    path('business/<mtaa_id>', views.business, name='business'),
    path('post/<mtaa_id>', views.post, name='post'),
    path('search/', views.search, name='search'),
]