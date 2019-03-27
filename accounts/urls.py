from django.urls import path

from accounts import views

urlpatterns = [
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
	path('profile/', views.profile, name='profile'),
	path('profile/edit_profile/', views.edit_profile, name='edit_profile')
]
