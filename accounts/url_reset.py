from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('password_change/',
         auth_views.PasswordChangeView.as_view(), name='password_change'),

]
