from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.index, name= 'index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('search', views.search, name='search'),
    path('movie/<str:pk>/', views.movie, name='movie'),
    path('genre/<slug:slug>/', views.movies_by_genre, name='movies_by_genre'),
    path('my-list', views.my_list, name= 'my-list'),
    path('add-to-list/', views.add_to_list, name='add-to-list'),
    path('remove-from-list/', views.remove_from_list, name='remove-from-list'),
    path('movie-recommendation/', views.movie_recommendation, name='movie_recommendation'),
    path('chat/', views.chat, name='chat'),
    path('visualizations/', views.visualization_view, name='visualizations'),
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),
    path('edit_customer/', views.edit_customer, name='edit_customer'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/<int:pk>/review/', views.add_review, name='add_review'),
    path('customer-report/', views.customer_report, name='customer_report'),
    path('top-movies-report/', views.top_movies_report, name='top_movies_report'),
]