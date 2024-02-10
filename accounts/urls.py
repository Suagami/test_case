from django.urls import path

from . import views

urlpatterns = [
    # post views
    path('account/logout/', views.user_logout, name='logout'),
    path('account/login/', views.user_login, name='login'),
    path('', views.index, name='index'),
    path("account/signup/", views.signup, name="signup"),
]